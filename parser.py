from rply_mod import ParserGenerator
from astr import Number, Sum, Sub, Mul, Div, Mod, AritPriority, Print, Scan, \
                LessThan, LessThanEqual, MoreThan, MoreThanEqual, IsEqual, IsNotEqual, \
                Ambient, AmbientGet


class PythonSimpleCalculatorParsingError(Exception):
    pass


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'SCAN', 'OPEN_PAREN', 'CLOSE_PAREN', 'SUM', 
             'SUB', 'MUL', 'DIV', 'MOD', 'LTH', 'MTH', 'LTE', 'MTE', 'DIF', 
             'ISE', 'ASSIGN', 'IDENTIFIER'])

    def parse(self, ambient : dict):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def program(p):
            return Print(p[2])
        @self.pg.production('program : expression')
        def program(p):
            return Print(p[0])
        @self.pg.production('program : compare')
        def program(p):
            return Print(p[0])
        @self.pg.production('program : IDENTIFIER ASSIGN expression')
        def program(p):
            return Ambient(p[0].value, p[2], ambient)


        @self.pg.production('compare : expression LTH expression')
        @self.pg.production('compare : expression MTH expression')
        @self.pg.production('compare : expression LTE expression')
        @self.pg.production('compare : expression MTE expression')
        @self.pg.production('compare : expression DIF expression')
        @self.pg.production('compare : expression ISE expression')
        def comparisson(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            match operator.gettokentype():
                case 'LTH':
                    return LessThan(left, right)
                case 'MTH':
                    return MoreThan(left, right)
                case 'LTE':
                    return LessThanEqual(left, right)
                case 'MTE':
                    return MoreThanEqual(left, right)
                case 'DIF':
                    return IsNotEqual(left, right)
                case 'ISE':
                    return IsEqual(left, right)


        @self.pg.production('expression : term SUM expression')
        @self.pg.production('expression : term SUB expression')
        @self.pg.production('expression : term')
        def expression(p):
            if len(p) == 1:
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
        @self.pg.production('term : factor MOD term')
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
            elif operator.gettokentype() == 'MOD':
                return Mod(left, right)
            

        @self.pg.production('factor : NUMBER')
        def factor(p):
            return Number(p[0].value, '+')
        
        @self.pg.production('factor : IDENTIFIER')
        def factor(p):
            return Number(AmbientGet(p[0].value, ambient).eval(), '+')
        
        @self.pg.production('factor : SUB NUMBER')
        @self.pg.production('factor : SUM NUMBER')
        def factor(p):
            return Number(p[1].value, "+" if p[0] == 'SUM' else '-') 
        
        @self.pg.production('factor : SCAN')
        def factor(p):
            return Scan()
        
        @self.pg.production('factor : OPEN_PAREN expression CLOSE_PAREN')
        def arithmetic_priority(p):
            return AritPriority(p[1])


        @self.pg.error
        def error_handle(token, position, tokens):
            input_str = ""
            for token in tokens:
                input_str += str(token.value)
            spacing = ' '*(position)
            raise PythonSimpleCalculatorParsingError(f"Erro de parsing: Encontrado token '{input_str[position]}' inesperado na posição {str(position)}.\
                                                     \n{str(input_str)}\n{spacing}^\n")

    def get_parser(self):
        return self.pg.build()