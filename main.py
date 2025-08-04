#expressões respeitando procedencia
#atribuição
#leitura e impressão
#numeros decimais

from lexer import Lexer

text_input = """test := 12.4;"""

lexer = Lexer()
lexer = lexer.get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)