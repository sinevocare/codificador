import string


class Teclado(object):
    dicionario = {
        'A': '2',
        'B': '22',
        'C': '222',
        'D': '3',
        'E': '33',
        'F': '333',
        'G': '4',
        'H': '44',
        'I': '444',
        'J': '5',
        'K': '55',
        'L': '555',
        'M': '6',
        'N': '66',
        'O': '666',
        'P': '7',
        'Q': '77',
        'R': '777',
        'S': '7777',
        'T': '8',
        'U': '88',
        'V': '888',
        'W': '9',
        'X': '99',
        'Y': '999',
        'Z': '9999',
        ' ': '0'
    }

    @classmethod
    def codificar(cls, mensagem):
        if type(mensagem) is not str:
            raise TypeError('Mensagem deve ser string.')

        if any(letra not in string.ascii_letters + ' ' for letra in mensagem):
            raise ValueError('A mensagem só deve possuir caracteres válidos.')

        if len(mensagem) > 255:
            raise ValueError('A mensagem deve possuir até 255 caracteres.')

        return ''.join(cls.dicionario[letra] for letra in mensagem)
