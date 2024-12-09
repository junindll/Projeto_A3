from client_manager import adicionar_cliente, atualizar_cliente, listar_cliente, apagar_cliente

adicionar_cliente('Maria Silva', 'maria@gmail.com', '123456789', 'Rua A, 123')

listar_cliente()

atualizar_cliente(1, 'Maria Silva', 'maria.silva@gmail.com', '987654321', 'Rua B, 456')

apagar_cliente(1)