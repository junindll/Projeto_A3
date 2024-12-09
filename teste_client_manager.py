import unittest
from client_manager import adicionar_cliente, atualizar_cliente, listar_cliente, apagar_cliente

class TestClientManager(unittest.TestCase):

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        # Cria um cliente base para os testes
        self.cliente_testes = {
            "nome": "Cliente Teste",
            "email": "teste@exemplo.com",
            "telefone": "123456789",
            "endereco": "Rua A, 123"
        }
        adicionar_cliente(**self.cliente_testes)

    def tearDown(self):
        """Limpa todos os registros do banco após os testes."""
        clientes = listar_cliente()
        for cliente in clientes:
            apagar_cliente(cliente[0])

    def test_adicionar_cliente(self):
        """Testa a adição de um cliente."""
        clientes = listar_cliente()
        self.assertGreater(len(clientes), 0, "Nenhum cliente foi adicionado")
        self.assertEqual(clientes[0][1], self.cliente_testes["nome"], "O nome do cliente não corresponde")

    def test_atualizar_cliente(self):
        """Testa a atualização de um cliente."""
        clientes = listar_cliente()
        id_cliente = clientes[0][0]

        dados_atualizados = {
            "id": id_cliente,
            "nome": "Teste Atualizado",
            "email": "teste@atualizado.com",
            "telefone": "999999999",
            "endereco": "Nova Rua 123"
        }
        atualizar_cliente(**dados_atualizados)

        clientes_atualizados = listar_cliente()
        cliente_atualizado = [c for c in clientes_atualizados if c[0] == id_cliente][0]

        self.assertEqual(cliente_atualizado[1], "Teste Atualizado", "Nome não foi atualizado corretamente")
        self.assertEqual(cliente_atualizado[2], "teste@atualizado.com", "E-mail não foi atualizado corretamente")

    def test_listar_cliente(self):
        """Testa se a função de listar clientes retorna clientes."""
        clientes = listar_cliente()
        self.assertGreater(len(clientes), 0, "Nenhum cliente foi listado")

    def test_apagar_cliente(self):
        """Testa a exclusão de um cliente."""
        clientes = listar_cliente()
        id_cliente = clientes[0][0]
        apagar_cliente(id_cliente)

        clientes_restantes = listar_cliente()
        self.assertFalse(any(c[0] == id_cliente for c in clientes_restantes), "O cliente não foi apagado")

if __name__ == "__main__":
    unittest.main()
