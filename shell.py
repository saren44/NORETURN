import sys
import noreturn


filename = sys.argv[1]
commands = []

with open(filename, "r") as f:
    lex = noreturn.Lexer(f.read())
    tokens = lex.make_tokens()
    #print(tokens)
    controller = noreturn.Controller(tokens)
