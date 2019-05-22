from sys import *

tokens = []

def open_file(filename):
    print("working...")
    data = open(filename, "r").read()
    return data

# Lexer figures out what kinds of keywords and values are in the source code
# and passes this to the compiler
def lex(filecontents):
    token = ""
    state = 0
    currentstring = ""

    filecontents = list(filecontents)

    for char in filecontents:
        token += char
        # ignore spaces
        if(token == " "):
            if state == 0:
                token = ""
            else:
                token = " "
        # ignore newlines
        elif token == "\n":
            token = ""
        #  keywords
        elif token == "PRINT":
            tokens.append("PRINT")
            token = ""
        # strings
        elif token == "\"":
            if state == 0:
                # first quote, start of string
                state = 1
                # token = ""
            elif state == 1:
                # 2nd quote, end of string, reset string and quote state
                tokens.append("STRING:" + currentstring + "\"")
                currentstring = ""
                state = 0
                token = ""
        elif state == 1:
            # between quotes, gather chars to the string
            currentstring += token
            token = ""

    print(tokens)
            


def run():
    data = open_file(argv[1])
    lex(data)


run()