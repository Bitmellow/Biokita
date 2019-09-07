from src.lexer import Lexer
from src.parser import Parser

class getFrom(object):
    def __init__(self, path):
        archive = open(path, 'r').read()

        lex = Lexer(archive)
        tokens = lex.tokenize()
        parser = Parser(tokens)

        parser.parse()