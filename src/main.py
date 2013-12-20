# -*- coding: utf-8 -*-
import ply.lex as lex

reserved = {
            'quote': 'QUOTE', 
            'atom': 'ATOM', 
            'eq': 'EQ', 
            'car': 'CAR', 
            'cdr': 'CDR', 
            'cons': 'CONS', 
            'cond': 'COND'
        }

tokens = ['LIST'] + list(reserved.values())

literals = ['(', ')', '\'']

def t_LIST(t):
    r'\w+'
    t.type = reserved.get(t.value, 'LIST')
    t.value = str(t.value)
    return t

t_ignore = ' \t'

def t_error(t):  
    print("Illegal character '%s'" % t.value[0])  
    t.lexer.skip(1)


lexer = lex.lex()
data = raw_input()
lexer.input(data)
for token in lexer:
    print token
