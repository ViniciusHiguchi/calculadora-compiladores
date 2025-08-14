#expressões respeitando procedencia
#atribuição
#leitura e impressão
#numeros decimais

from lexer import Lexer
from parser import Parser

lexer = Lexer()
lexer = lexer.get_lexer()

pg = Parser()
pg.parse()
parser = pg.get_parser()

while True:
    text_input = input('>> ')
    tokens = lexer.lex(text_input)
    try:
        parser.parse(tokens).eval()
    except Exception as e:
        print(e)