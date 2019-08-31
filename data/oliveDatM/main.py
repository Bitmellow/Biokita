import lexer
import parser

archive = open("data/oliveDatM/test.tso", 'r').read()

lex = lexer.Lexer(archive)
tokens = lex.tokenize()
print(tokens)