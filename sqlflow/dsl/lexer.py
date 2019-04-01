# coding=utf-8

import ply.lex as lex

# List of token names.
reversed = (
    # Main
    'CREATE', 'TABLE', 'DROP', 'SHOW', 'ALTER', 'SELECT', 'FROM', 'WHERE',
    'INSERT', 'DELETE', 'UPDATE', 'VIEW', 'USER', 'REVOKE', 'GRANT',
    'INDEX', 'LOAD', 'SET', 'INTO', 'VALUES', 'TABLES', 'ALERT', 'ADD', "ON",
    "TO", 'LIMIT',
    'PASSWORD',
    # Modifier
    'PRIMARY', 'KEY', 'DESC', 'ASC', 'ALL',
    # Const Value
    'NULL',
    # Command
    'HELP', 'PRINT', 'EXIT', 'SPARKSQL',
    # Operator
    'AND', 'OR', 'IS', 'NOT',
    # Type
    'INT', 'CHAR', 'AS',
    'TRAIN', 'REGISTER', 'SAVE', 'CONNECT', 'SET', 'OVERWRITE', 'JDBC',
)

tokens = reversed + (
    # Symbol
    'ID', 'NUMBER', 'STRING',
    # Operator
    'EQ', 'LT', 'LE', 'GT', 'GE', 'NE',
)

# Regular expression rules for simple tokens
t_EQ = r'='
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_NE = r'!='

literals = ['(', ')', ',', ';', '.', '+', '-', '*', '/']

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
