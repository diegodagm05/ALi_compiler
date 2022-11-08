# ------------------------------------------------------------
# lexer.py
#
# tokenizer for ALi language
# ------------------------------------------------------------
import ply.lex as lex
# Reserved words
reserved = {
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'array': 'ARRAY',
    'bool': 'BOOL',
    'void': 'VOID',
    'func': 'FUNC',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'elif': 'ELIF',
    'return': 'RETURN',
    'print': 'PRINT',
    'read': 'READ',
    'for': 'FOR',
    'while': 'WHILE',
    'read': 'READ',
    'true': 'TRUE',
    'false': 'FALSE',
    # Game Engine specific tokens
    'start': 'START',
    'update': 'UPDATE',
    'generateCanvas': 'GEN_CANVAS',
    'setCanvasTitle': 'SET_CANVAS_TITLE',
    'setCanvasBackground': 'SET_CANVAS_BG',
    'getWindowHeight': 'GET_WINDOW_H',
    'getWindowWidth': 'GET_WINDOW_W',
    'getGameEvent': 'GET_GAME_EV',
    'drawGameObject': 'DRAW_GAME_OBJECT',
}
# TODO: List of token names
tokens = (
   'I_CONST', 'F_CONST', 'C_CONST', 'STRING_CONST', 'ID', 'DIFFERENT', 'EQUAL', 'AND', 'OR', 'GREATER_EQ', 'LESS_EQ'
) + tuple(reserved.values())

# literal symbols
literals = [';', ',', ':', '.', '{', '}', '(', ')', '[', ']', '=', '+', '-', '*', '/', '>', '<', '!']


# Token regular expressions
t_STRING_CONST = r'\"([^\\]|(\\.))*?\"'
t_DIFFERENT = r'\!\='
t_EQUAL = r'\=\='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_GREATER_EQ = r'\>\='
t_LESS_EQ = r'\<\='

#  Complex tokens
def t_F_CONST(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t
    
def t_I_CONST(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_C_CONST(t):
    r'\'[0-9A-Za-z_ ]{1}\''
    t.value = list(t.value)[1]
    return t


def t_ID(t):
    r'[A-Za-z]([A-Za-z] | [0-9] | \_)*'
    if t.value not in reserved:
        t.type = 'ID'
    else:
        t.type = reserved[t.value]
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
# Ignore comments
t_ignore_COMMENT = r'\/\/.*'


# Error handling rule
def t_error(t):
    print(t)
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def test():
    print('Testing')
    file = open('./test_files/helloWorld.al')
    input_str = file.read()
    file.close()
    lexer.input(input_str)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)


if __name__ == '__main__':
    test()