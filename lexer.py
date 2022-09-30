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
    'void': 'VOID',
    'func': 'FUNC',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'print': 'PRINT',
    'read': 'READ',
    'for': 'FOR',
    'until': 'UNTIL',
    'while': 'WHILE'
}
# TODO: List of token names
tokens = (
   'CTE_I', 'CTE_F', 'CTE_STRING', 'ID', 'DIFFERENT'
) + tuple(reserved.values())

# literal symbols
literals = [';', ',', ':', '.', '{', '}', '(', ')', '[', ']', '=', '+', '-', '*', '/', '>', '<', '!', '&', '|']


# Token regular expressions
t_CTE_STRING = r'\"[0-9A-Za-z_ ]*\"'
t_DIFFERENT = r'\!\='

#  Complex tokens
def t_CTE_F(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
    
def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTE_C(t):
    r'\'[0-9A-Za-z_ ]{1}\''
    t.value = chr(t.value)
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

# Error handling rule
def t_error(t):
    print(t)
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def test():
    print('Testing')
    file = open('hello_world.ld')
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