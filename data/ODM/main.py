from src import lexer
from src import parser

archive = open("data/oliveDatM/test.tso", 'r').read()

lex = lexer.Lexer(archive)
tokens = lex.tokenize()
pars = parser.Parser(tokens)
print(tokens)