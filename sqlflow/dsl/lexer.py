# coding=utf-8

import ply.lex as lex

# List of token names.
reversed = (
    # Main
    'LOAD', 'HELP', 'SSQL', 'WHERE','AND','AS',
    'TRAIN', 'REGISTER', 'SAVE', 'CONNECT', 'SET', 'OVERWRITE',
    # Scikit-learn
    'SKLEARN', 'KNN'
)

tokens = reversed + (
    # Symbol
    'ID', 'NUMBER', 'STRING',
    # Operator
    'EQ',
)

# Regular expression rules for simple tokens
t_EQ = r'='

literals = ['(', ')', ',', ';', '.']

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Ignore note
t_ignore_note = r'\/\*.*?\*/'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID' if t.value.upper() not in reversed else t.value.upper()  # Check for reserved words
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'(\'|").*?(\'|")'
    t.value = t.value[1: -1]
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("LexError [%s, %s]: Illegal character '%s'." % (
        t.lexer.lineno, t.lexer.lexpos, t.value[0]))


lexer = lex.lex()

if __name__ == '__main__':
    data = input('Lexer > ')
    # lexer = lex.lex()
    # lexer.input(data)
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break
    #     print(tok)
