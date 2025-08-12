from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('MOD', r'\%')

        # Operators rel
        self.lexer.add('LTH', r'\<')
        self.lexer.add('MTH', r'\>')
        self.lexer.add('LTE', r'\<\=')
        self.lexer.add('MTE', r'\>\=')
        self.lexer.add('DIF', r'\!\=')
        self.lexer.add('ISE', r'\=\=')

        # id
        # Number
        self.lexer.add('NUMBER', r'\d+(\.\d+)?')

        # Ignore spaces
        self.lexer.ignore(r'\s+')

        # Commands
        self.lexer.add('ASSIGN', r':=')
        self.lexer.add('PRINT', r'print')
        self.lexer.add('SCAN', r'scan')

        #id
        self.lexer.add('IDENTIFIER', "[a-zA-z_][a-zA-z_0-9_]*")



    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()