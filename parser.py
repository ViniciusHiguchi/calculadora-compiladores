from rply import ParserGenerator
from astr import Number, Sum, Sub, Mul, Div, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'MOD']
        )


    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : term SUM expression')
        @self.pg.production('expression : term SUB expression')
        @self.pg.production('expression : term')
        def expression(p):
            if len(p) == 1:
                print(p[0])
                return p[0]
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator:
                if operator.gettokentype() == 'SUM':
                    return Sum(left, right)
                elif operator.gettokentype() == 'SUB':
                    return Sub(left, right)
            
        @self.pg.production('term : factor MUL term')
        @self.pg.production('term : factor DIV term')
        @self.pg.production('term : factor')
        def term(p):
            if len(p) == 1:
                return p[0]
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            
        @self.pg.production('factor : NUMBER')
        def factor(p):
            return Number(p[0].value)
        
        #@self.pg.production('factor : OPEN_PAREN expression CLOSE_PAREN')
        #@self.pg.production('factor : OPEN_PAREN term CLOSE_PAREN')
        #def arithmetic_priority(p):
        #    return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()