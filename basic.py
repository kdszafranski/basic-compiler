from sys import *

tokens = []

def open_file(filename):
    data = open(filename, "r").read()
    return data

# Lexer figures out what kinds of keywords and values are in the source code
# and passes this to the compiler
def lex(filecontents):
    token = ""
    state = 0
    expression = 0
    currentstring = ""
    currentexpression = ""

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
            print("new line")
            token = ""
            if expression == 1:
                print("ending expression")
                tokens.append("EXP:" + currentexpression)
                currentexpression = ""
                expression = 0
        #  keywords
        elif token.upper() == "PRINT":
            tokens.append("PRINT")
            token = ""
        # numbers/expressions
        # 8
        # 10
        # 10 +-/*
        elif token.isnumeric():
            print("numeric: " + token)
            if expression == 0:
                print("new expression")
                expression = 1
                currentexpression += token
                print(currentexpression)
                token = ""
            elif expression == 1:
            #     # print(currentexpression)
                currentexpression += token
            #     expression = 0
        # strings
        elif token == "\"":
            if state == 0:
                # first quote, start of string
                state = 1
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
    # return tokens
    print(tokens)


def parse(tokens):
    # print(tokens) 
    i = 0
    while(i < len(tokens)):
        # print(tokens[i])
        if tokens[i] == "PRINT":
            # print something
            if tokens[i + 1][0:6] == "STRING":
                # print string
                print(tokens[i + 1][7:])
        i += 2
    # end while



def run():
    data = open_file(argv[1])
    # lexer
    tokens = lex(data)
    # pass lex result to parser
    # parse(tokens)


run()