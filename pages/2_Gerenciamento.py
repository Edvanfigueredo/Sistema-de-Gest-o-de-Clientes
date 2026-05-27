import streamlit as st
import pandas as pd

st.title("Gerenciamento de Clientes")
st.divider()

dados = pd.read_csv("clientes.csv")

if not dados.empty:
    
    cliente_selecionado = st.selectbox("Selecione um cliente para editar ou excluir:",
                                      options=dados["nome"])
if st.button("Editar Cliente"):
        st.write(f"Editar cliente: {cliente_selecionado}")
        # Lógica para editar o cliente selecionado
        st.write("Formulário para edição do cliente")
        nome_novo = st.text_input("Digite o novo nome do cliente:", key="nome_novo")
        dt_nasc_novo = st.date_input("Digite a nova data de nascimento do cliente:", format="DD/MM/YYYY", key="dt_nasc_novo")
        tipo_cliente_novo = st.selectbox("Selecione o novo tipo de cliente:", options=["Pessoa Física", "Pessoa Jurídica"], key="tipo_cliente_novo")
        if st.button("Salvar Alterações"):
            dados.loc[dados["nome"] == cliente_selecionado, ["nome", "dt_nasc", "tipo_cliente"]] = [nome_novo, dt_nasc_novo, tipo_cliente_novo]
            dados.to_csv("clientes.csv", index=False)
            st.success("Cliente editado com sucesso!", icon="✅")
            st.radio("Atualizar a lista de clientes:", options=["Sim", "Não"], index=0, key="atualizar_lista")
            if st.session_state["atualizar_lista"] == "Sim":
                st.experimental_rerun()
        dados_atualizados = dados[dados["nome"] != cliente_selecionado]
else:
     st.info("Nenhum cliente cadastrado. Por favor, cadastre um cliente para gerenciar.", icon="ℹ️")
     
if st.button("Excluir Cliente"):
        st.write(f"Excluir cliente: {cliente_selecionado}")
        # Lógica para excluir o cliente selecionado
        dados_atualizados = dados[dados["nome"] != cliente_selecionado]

        dados_atualizados.to_csv("clientes.csv", index=False)
        st.success("Cliente excluído com sucesso!", icon="✅")
        st.radio("Atualizar a lista de clientes:", options=["Sim", "Não"], index=0, key="atualizar_lista")
        if st.session_state["atualizar_lista"] == "Sim":
            st.experimental_rerun()
else:
    st.info("Nenhum cliente cadastrado. Por favor, cadastre um cliente para gerenciar.", icon="ℹ️")