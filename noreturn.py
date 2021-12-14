import pointers


# TOKENS

TT_SWAP = "SWAP"
TT_MOVE = "MOVE"
TT_ADD = "ADD"
TT_SUB = "SUB"
TT_COPY = "COPY"
TT_PRINT = "PRINT"
TT_READ = "READ"
TT_LOOP_START = "LOOP_START"
TT_LOOP_END = "LOOP_END"
TT_PRINT_CHAR = "PRINT_CHAR"
#TT_COMMENT = "COMMENT"


class Token:
    def __init__(self, t):
        self.type = t

    def __repr__(self):
        return f'{self.type}'

# LEXER

commands = {
    "sp": TT_SWAP,
    "mv": TT_MOVE,
    "add": TT_ADD,
    "sub": TT_SUB,
    "cp": TT_COPY,
    "pr": TT_PRINT,
    "rd": TT_READ,
    "ls": TT_LOOP_START,
    "le": TT_LOOP_END,
    "prc": TT_PRINT_CHAR,
#   "#": 7
}


class Lexer:

    def __init__(self, text):
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
        self.text = text.split(" ")

    def make_tokens(self):
        tokens = []
        commented = False

        for word in self.text:
            if word in commands.keys():
                tokens.append(Token(commands[word]))

        return tokens

# CONTROLLER


class Controller:

    def __init__(self, tokens, space=None, active=None, inactive=None):
        if space is None:
            space = [0]
        self.tokens = tokens
        self.space = space
        if active is None and inactive is None:
            self.active = pointers.Pointer()
            self.inactive = pointers.Pointer()
        else:
            self.active = active
            self.inactive = inactive
        self.solve_tokens()

    def move(self):
        self.active.move()
        if self.active.value == len(self.space):
            self.space.append(0)

    def swap(self):
        self.active, self.inactive = self.inactive, self.active

    def add(self):
        self.space[self.active.value] += 1

    def sub(self):
        self.space[self.active.value] -= 1

    def copy(self):
        self.space[self.active.value] = self.space[self.inactive.value]

    def print(self):
        print(self.space[self.active.value])

    def print_char(self):
        print(chr(self.space[self.active.value]), end="")

    def read(self):
        self.space[self.active.value] = int(input())

    def loop(self, aux):
        #print(aux, self.space[self.active.value])
        for i in range(self.space[self.active.value]):
            sub_controller = Controller(aux, self.space, self.active, self.inactive)
            self.space = sub_controller.space
            self.active = sub_controller.active
            self.inactive = sub_controller.inactive
            #print(self.space, self.active.value)

    def solve_tokens(self):
        loop_aux = []
        looping = False
        nested = 0
        for token in self.tokens:
            if not looping:
                if token.type == "MOVE":
                    self.move()
                elif token.type == "SWAP":
                    self.swap()
                elif token.type == "ADD":
                    self.add()
                elif token.type == "SUB":
                    self.sub()
                elif token.type == "COPY":
                    self.copy()
                elif token.type == "PRINT":
                    self.print()
                elif token.type == "PRINT_CHAR":
                    self.print_char()
                elif token.type == "READ":
                    self.read()
                elif token.type == "LOOP_START":
                    nested = 0
                    looping = True
            elif token.type == "LOOP_START":
                loop_aux.append(token)
                nested += 1
            elif token.type == "LOOP_END":
                if nested == 0:
                    self.loop(loop_aux)
                    loop_aux = []
                    looping = False
                else:
                    nested -= 1
                    loop_aux.append(token)
            else:
                loop_aux.append(token)