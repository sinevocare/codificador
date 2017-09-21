import unittest

from codificador.telefone import Teclado


class TecladoTestCase(unittest.TestCase):
    def testa_se_entrada_eh_string(self):
        with self.assertRaises(TypeError):
            Teclado.codificar(42)


if __name__ == '__main__':
    unittest.main()
