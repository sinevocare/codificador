import string


class Teclado(object):
    @classmethod
    def codificar(cls, mensagem):
        if type(mensagem) is not str:
            raise TypeError('Mensagem deve ser string.')

        if any(letra not in string.ascii_letters + ' ' for letra in mensagem):
            raise ValueError('A mensagem só deve possuir caracteres válidos.')

        if len(mensagem) > 255:
            raise ValueError('A mensagem deve possuir até 255 caracteres.')
