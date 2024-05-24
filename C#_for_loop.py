#FOR LOOP
import ply.lex as lex
import ply.yacc as yacc

# Lex code
tokens = (
    'ID',
    'LPAREN',
    'RPAREN',
    'SEMI_COLON',
    'INT_TYPE',
    'EQUALS',
    'LESS_THAN',
    'PLUS',
    'MINUS',
    'NUMBER',
    'FOR',
)

t_LPAREN= r'\('
t_RPAREN= r'\)'
t_SEMI_COLON=r';'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_EQUALS=r'='
t_LESS_THAN=r'<'
t_NUMBER=r'\d+'
t_INT_TYPE = r'\d+'
t_FOR=r'for'

t_ignore=r' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser rules
def p_statement(p):
    '''
    statement : for_loop
    '''
    print("Statement:", p[1])

def p_for_loop(p):
    '''
    for_loop : FOR LPAREN initialization SEMI_COLON condition SEMI_COLON increment RPAREN
    '''
    p[0] = f"For loop with initialization: {p[3]}, condition: {p[5]}, and increment: {p[7]}"

def p_initialization(p):
    '''
    initialization : INT_TYPE ID EQUALS NUMBER
    '''
    p[0] = f"Initialize {p[2]} with {p[4]}"

def p_condition(p):
    '''
    condition : ID LESS_THAN NUMBER
    '''
    p[0] = f"Check if {p[1]} is less than {p[3]}"

def p_increment(p):
    '''
    increment : ID PLUS PLUS
            | ID MINUS MINUS
    '''
    p[0] = f"Increment {p[1]}"

def p_error(p):
    if p:
        print(f"Syntax error: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# data = '''
#     for (int i = 0; i < 10; i++)
#     {
#         // Do something
#     }
# '''

data='''
    for(int i=0;i<n;i++)'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)