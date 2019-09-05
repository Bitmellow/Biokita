from src import lexer
from src import parser

archive = open("data/ODM/test.tso", 'r').read()

lex = lexer.Lexer(archive)
tokens = lex.tokenize()
parser = parser.Parser(tokens)

parser.parse()