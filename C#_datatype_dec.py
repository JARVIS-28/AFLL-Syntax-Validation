# SIMPLE DATATYPE DECLARATION
import ply.lex as lex
import ply.yacc as yacc

# Lex code
tokens = (
    'ID',
    'COLON',
    'SEMICOLON',
    'INT_TYPE',
    'FLOAT_TYPE',
    'STRING_TYPE',
)
t_SEMICOLON=r';'
t_COLON= r':'
t_INT_TYPE = r'int'
t_FLOAT_TYPE = r'float'
t_STRING_TYPE = r'string'
t_ID= r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = ' \t\n'

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc code
def p_declaration(p):
    '''
    declaration : type ID SEMICOLON
    '''
    print(f"Declaration: {p[2]} is of type {p[1]}")

def p_type(p):
    '''
    type : INT_TYPE
            | FLOAT_TYPE
            | STRING_TYPE
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

# Test the parser
# data='''
    
#     string w;
#     float x;
#     int q;
# '''

data= '''
string x;
'''
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)


