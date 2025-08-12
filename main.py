#expressões respeitando procedencia
#atribuição
#leitura e impressão
#numeros decimais

from lexer import Lexer
from parser import Parser

text_input = "print(1*12*12*10+15+20*10+5+1+1+1+1+1+1);"

lexer = Lexer()
lexer = lexer.get_lexer()
tokens = lexer.lex(text_input)

#for token in tokens:
#    print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()