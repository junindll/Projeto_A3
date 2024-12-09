import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='sistema_clientes',
            user='root',
            password=''
        )

        if connection.is_connected():
            print("Sua conexão com o MySQL foi bem sucedida!")
            return connection
        else:
            print("Falha na conexão com o MySQL.")
            return None

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
    