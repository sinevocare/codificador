import unittest

from codificador.telefone import Teclado


class TecladoTestCase(unittest.TestCase):
    def testa_se_entrada_eh_string(self):
        with self.assertRaises(TypeError):
            Teclado.codificar(42)

    def testa_se_entrada_possui_caracteres_validos(self):
        with self.assertRaises(ValueError):
            Teclado.codificar('E aí, bebê')


if __name__ == '__main__':
    unittest.main()
