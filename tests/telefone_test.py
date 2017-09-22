import unittest

from codificador.telefone import Teclado


class TecladoTestCase(unittest.TestCase):
    def testa_se_entrada_eh_string(self):
        with self.assertRaises(TypeError):
            Teclado.codificar(42)

    def testa_se_entrada_possui_caracteres_validos(self):
        with self.assertRaises(ValueError):
            Teclado.codificar('E aí, bebê')

    def testa_se_entrada_possui_ate_255_caracteres(self):
        with self.assertRaises(ValueError):
            Teclado.codificar(
                'Lorem ipsum dolor sit amet consectetur adipiscing '
                'elit proin finibus velit in metus congue a iaculis '
                'odio varius maecenas sollicitudin consectetur '
                'fermentum duis pellentesque vestibulum eros et '
                'blandit phasellus pharetra neque pretium ultricies '
                'a facilisis'
            )

    def testa_entrada_valida_com_uma_letra(self):
        self.assertEqual('7777', Teclado.codificar('S'))

    def testa_entrada_valida_com_letras_de_mesmo_numero(self):
        self.assertEqual('7_777', Teclado.codificar('PR'))


if __name__ == '__main__':
    unittest.main()
