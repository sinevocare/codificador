# Plano de testes

Desenvolvido por Albert Morato e Guilherme Portela.

## Identificação

### Objetivo
Desenvolver cultura de práticas de desenvolvimento com teste unitário.

### Problema
Um dos serviços mais utilizados pelos usuários de aparelhos celulares são os SMS (Short Message Service), que permite o envio de mensagens curtas (até 255 caracteres em redes GSM e 160 caracteres em redes CDMA).

Para digitar uma mensagem em um aparelho que não possui um teclado QWERTY embutido é necessário fazer algumas combinações das 10 teclas numéricas do aparelho para conseguir digitar. Cada número é associado a um conjunto de letras como a seguir:

| Letras | Número |
|--------|--------|
| ABC    | 2      |
| DEF    | 3      |
| GHI    | 4      |
| JKL    | 5      |
| MNO    | 6      |
| PQRS   | 7      |
| TUV    | 8      |
| WXYZ   | 9      |
| Espaço | 0      |

Desenvolva um programa que, dada uma mensagem de texto limitada a 255 caracteres, retorne a seqüência de números que precisa ser digitada. Uma pausa, para ser possível obter duas letras referenciadas pelo mesmo número, deve ser indicada como _.


## Classes de equivalência

| Entrada   | Condição                   | Classes Válidas                                                   | Classes Inválidas                                                     |
|-----------|----------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------|
| `message` | É uma string               | (1) `type(message) is str`                                        | (4) `type(message) is not str`                                        |
|           | Só possui letras e espaços | (2) `all(char in string.ascii_letters + ' ' for char in message)` | (5) `any(char not in string.ascii_letters + ' ' for char in message)` |
|           | Possui até 255 caracteres  | (3) `len(message) <= 255`                                         | (6) `len(message) > 255`                                              |


## Casos de teste

| #  | Classes 	| Message                                                                                                                                                                                                                                                              | Saída Esperada                          |
|----|---------	|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| 1  | 1, 2, 3 	| `'S'`                                                                                                                                                                                                                                                                | `'7777'`                                |
| 2  | 1, 2, 3 	| `'PR'`                                                                                                                                                                                                                                                               | `'7_777'`                               |
| 3  | 1, 2, 3 	| `'e ai'`                                                                                                                                                                                                                                                             | `'3302444'`                             |
| 4  | 1, 2, 3 	| `'SEMPRE ACESSO'`                                                                                                                                                                                                                                                    | `'77773367_7773302_222337777_77776660'` |
| 5  | 4       	| `42`                                                                                                                                                                                                                                                                 | Lança exceção                           |
| 6  | 5       	| `'E aí, bebê'`                                                                                                                                                                                                                                                       | Lança exceção                           |
| 7  | 6       	| `'Lorem ipsum dolor sit amet consectetur adipiscing elit proin finibus velit in metus congue a iaculis odio varius maecenas sollicitudin consectetur fermentum duis pellentesque vestibulum eros et blandit phasellus pharetra neque pretium ultricies a facilisis'` | Lança exceção                           |


## Fonte

O problema foi encontrado e descrito em [DojoPuzzles.com](http://dojopuzzles.com/problemas/exibe/escrevendo-no-celular/).
