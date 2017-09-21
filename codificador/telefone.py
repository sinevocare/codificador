class Teclado(object):
    @classmethod
    def codificar(cls, mensagem):
        if type(mensagem) is not str:
            raise TypeError('Mensagem deve ser string.')
