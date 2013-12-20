# -*- coding: utf-8 -*-
import ply.lex as lex
import ply.yacc as yacc

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

literals = ['(', ')', '`']

def t_LIST(t):
    r'\w+'
    t.type = reserved.get(t.value, 'LIST')
    if t.type == 'LIST':
        _ = []
        _.append(str(t.value))
        t.value = _
    else:
        t.value = str(t.value)
    return t

t_ignore = ' \t'

def t_error(t):  
    print("Illegal character '%s'" % t.value[0])  
    t.lexer.skip(1)

def p_expression_all(p):
    '''
    expression : '`' LIST
               | '`' '(' fator ')'
               | '(' ATOM expression ')'
               | '(' QUOTE expression ')'
               | '(' CAR expression ')'
               | '(' CDR expression ')'
               | '(' COND expressionComplex ')'
               | '(' CONS expression expression ')'
               | '(' EQ expression expression ')'
    '''
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 5:
        if p[1] == '`':               p[0] = p[3]
        elif p[2] == 'quote':         p[0] = p[3]
        elif p[2] == 'car':           p[0] = p[3][0:1]
        elif p[2] == 'cdr':           p[0] = p[3][1:]
        elif p[2] == 'cond':
            ret = []
            for _ in len(p[3]):
                if 't' in p[3][_][0]:
                    ret = p[3][_][1]
                    break
            p[0] = ret
        else:
            if len(p[3]) == 1:            p[0] = 't'
            else:                         p[0] = 'NIL'
    elif len(p) == 6:
        if p[2] == 'cons':
            p[0] = p[3] + p[4]
        else:
             if set(p[3]) == set(p[4]):    p[0] = ['t']
             else:                         p[0] = []
             
                                      
def p_factor_expr(p):
    '''
    fator      : LIST
               | LIST fator
    '''
    if len(p) == 2:                   p[0] = p[1]
    else:                             p[0] = p[1] + p[2]

def p_expressionComplex_all(p):
    '''
    expressionComplex       : '(' expression expression ')'
                            | '(' expression expression ')' expressionComplex
    '''
    if len(p) == 5:
        _ = []
        _.append((p[2], p[3]))
        p[0] = _
    else:
        p[0] = p[5]
        p[5].append((p[2], p[3]))

def p_error(p):  
    if p:  
        print("Syntax error at '%s'" % p.value)  
    else:  
        print("Syntax error at EOF")


lexer = lex.lex()
yaccer = yacc.yacc()
while 1:
    try:
        _ = raw_input('LISP > ')
    except EOFError:
        break
    if not _:
        continue
    result = yacc.parse(_)
    print result
