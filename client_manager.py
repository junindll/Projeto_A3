from database import create_connection

def adicionar_cliente(nome, email, telefone, endereco):
    # Cria a conexão com o banco de dados
    connection = create_connection()
    if connection:
        try:
            # Cria um cursor para executar as queries SQL
            cursor = connection.cursor()
            cursor.execute(''' 
                INSERT INTO clientes (nome, email, telefone, endereco)
                VALUES (%s, %s, %s, %s)
            ''', (nome, email, telefone, endereco))
            connection.commit()  # Confirma a inserção no banco de dados
            print(f"Cliente {nome} cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar cliente: {e}")
        finally:
            cursor.close()
            connection.close()

def atualizar_cliente(id, nome, email, telefone, endereco):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE clientes
                SET nome = %s, email = %s, telefone = %s, endereco = %s
                WHERE id = %s
            ''', (nome, email, telefone, endereco, id))
            connection.commit()
            print(f"Cliente com ID {id} atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
        finally:
            cursor.close()
            connection.close()

def listar_cliente():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM clientes')
            clientes = cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

def apagar_cliente(cliente_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM clientes WHERE id = %s', (cliente_id,))
            connection.commit()
            print(f"Cliente com ID {cliente_id} deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
        finally:
            cursor.close()
            connection.close()

# Menu interativo
if __name__ == "__main__":
    while True:
        print("\n--- Menu de Ações ---")
        print("1. Adicionar Cliente")
        print("2. Listar Cliente")
        print("3. Atualizar Cliente")
        print("4. Apagar Cliente")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o e-mail do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            adicionar_cliente(nome, email, telefone, endereco)

        elif opcao == '2':
            clientes = listar_cliente()
            print("Clientes cadastrados:")
            for cliente in clientes:
                print(cliente)

        elif opcao == '3':
            id_cliente = int(input("Digite o ID do cliente a ser atualizado: "))
            nome = input("Digite o novo nome do cliente: ")
            email = input("Digite o novo e-mail do cliente: ")
            telefone = input("Digite o novo telefone do cliente: ")
            endereco = input("Digite o novo endereço do cliente: ")
            atualizar_cliente(id_cliente, nome, email, telefone, endereco)

        elif opcao == '4':
            id_cliente = int(input("Digite o ID do cliente a ser apagado: "))
            apagar_cliente(id_cliente)

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")
