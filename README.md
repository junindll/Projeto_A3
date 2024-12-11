# Projeto_A3 = Sistema de cadastro de clientes

Sistema simples de cadastro de clientes utilizando Python e MySQL. Permite adicionar, listar, atualizar e apagar clientes.

## Funcionalidades

- **Adicionar cliente**: Permite adicionar um novo cliente ao banco de dados.
- **Listar clientes**: Mostra todos os clientes cadastrados.
- **Atualizar cliente**: Permite alterar as informações de um cliente existente.
- **Deletar cliente**: Exclui um cliente do banco de dados.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem usada para programar o sistema.
- **MySQL**: Banco de dados utilizado para armazenar as informações dos clientes.
- **mysql-connector-python**: Biblioteca do Python para se conectar ao MySQL.

## O que você precisa para rodar o sistema?

1. **Python 3.x**: Se você ainda não tem o Python, você pode baixar e instalar [aqui](https://www.python.org/downloads/).
2. **MySQL**: Você precisa ter o MySQL instalado no seu computador. Se não tiver, baixe [aqui](https://dev.mysql.com/downloads/).
3. Instalar a biblioteca que o Python usa para se conectar ao MySQL. Para fazer isso, basta abrir o terminal e rodar o seguinte comando:
```
pip install mysql-connector-python
```
## Como configurar o banco de dados?

1. Abra o MySQL e crie um banco de dados chamado `sistema_clientes` com o seguinte comando:
```
CREATE DATABASE sistema_clientes;
```
2. Após criar o banco de dados, crie uma tabela chamada `clientes` para armazenar os dados. O código para criar a tabela é:
```
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(100)
);
```
## Como rodar o sistema?

1. Baixe ou clone o repositório do projeto para o seu computador.
2. Abra o arquivo `database.py` e verifique se as configurações de conexão com o MySQL estão corretas (seu usuário, senha e nome do banco de dados).

Para executar o programa, basta executar o `client_manager.py` e irá aparecer o menu de ações.


## Como usar o sistema?

Quando o programa for executado, ele vai mostrar um menu com várias opções. Você pode escolher uma opção digitando o número correspondente e seguir as instruções para adicionar, listar, atualizar ou excluir um cliente.






   


