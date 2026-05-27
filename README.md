# 📊 Sistema Web de Gestão de Clientes

Aplicação web desenvolvida em Python utilizando Streamlit para gerenciamento de cadastros de clientes.
O projeto foi criado como atividade prática de conclusão do curso **Dominando a Linguagem Python**, promovido pela Daxus.

A aplicação implementa operações completas de CRUD (*Create, Read, Update and Delete*), permitindo cadastrar, consultar, editar e remover registros de clientes de forma simples e intuitiva.

---

## 🚀 Funcionalidades

* Cadastro de clientes com formulário interativo;
* Seleção do tipo de cliente:

  * Pessoa Física;
  * Pessoa Jurídica;
* Validação de data de nascimento;
* Consulta dinâmica dos registros cadastrados;
* Edição de informações já existentes;
* Exclusão de registros;
* Persistência de dados em arquivo `.csv`;
* Interface web responsiva utilizando Streamlit.

---

## 📁 Estrutura do Projeto

```text
projetopratico/
│
├── Home.py
├── clientes.csv
│
├── pages/
│   ├── 1_Cadastro.py
│   ├── 2_Consulta.py
│   └── 3_Gerenciamento.py
│
└── README.md
```

### Descrição dos Arquivos

| Arquivo              | Função                        |
| -------------------- | ----------------------------- |
| `Home.py`            | Página principal da aplicação |
| `clientes.csv`       | Armazenamento local dos dados |
| `1_Cadastro.py`      | Cadastro de novos clientes    |
| `2_Consulta.py`      | Consulta dos registros        |
| `3_Gerenciamento.py` | Edição e exclusão de clientes |

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Streamlit**
* **Pandas**

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, é necessário possuir instalado:

* Python 3.10 ou superior;
* Pip atualizado.

---

## 🔧 Instalação e Execução

Clone o repositório:

```bash
git clone https://github.com/seuusuario/projetopratico.git
```

Acesse o diretório do projeto:

```bash
cd projetopratico
```

Instale as dependências:

```bash
pip install streamlit pandas
```

Execute a aplicação:

```bash
streamlit run Home.py
```

Após iniciar o servidor, o Streamlit disponibilizará automaticamente o endereço local no navegador.

---

## 📸 Interface da Aplicação

> Espaço destinado para imagens ou GIFs demonstrando o funcionamento do sistema.

Exemplo:

```text
assets/
├── home.png
├── cadastro.png
└── gerenciamento.png
```

---

## 🧠 Funcionamento da Aplicação

O sistema utiliza o Streamlit para construção da interface web e o Pandas para manipulação dos dados.

As informações cadastradas são armazenadas localmente em um arquivo CSV, permitindo persistência simples sem necessidade de banco de dados relacional.

O fluxo principal da aplicação consiste em:

1. Cadastro de clientes;
2. Armazenamento das informações;
3. Consulta dos registros;
4. Atualização ou remoção de dados.

---

## 📌 Possíveis Melhorias Futuras

* Integração com banco de dados SQL;
* Sistema de autenticação de usuários;
* Exportação de relatórios em PDF;
* Dashboard com métricas;
* Hospedagem em nuvem;
* Validações avançadas de formulário.

---

## 📄 Licença

Este projeto possui finalidade educacional e acadêmica.

---

## 👨‍💻 Autor

Desenvolvido por **Edvan Figuerêdo** como projeto prático para conclusão da trilha de fundamentos em Python.

