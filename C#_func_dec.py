# FUNCTION DECLARATION
import ply.lex as lex
import ply.yacc as yacc

# Lex code
tokens = (
    'ID',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMI_COLON',
    'INT_TYPE',
    'FLOAT_TYPE',
    'STRING_TYPE',
    'VOID_TYPE',
    'PUBLIC',
)

t_LPAREN= r'\('
t_RPAREN= r'\)'
t_COMMA= r','
t_SEMI_COLON=r';'
t_INT_TYPE = r'\d+'
t_FLOAT_TYPE = r'\d+\.\d+'
t_STRING_TYPE = r'"[^"]*"'
t_VOID_TYPE=r'void'
t_PUBLIC=r'public'

t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Yacc code
def p_function_declaration(p):
    '''
    function_declaration : PUBLIC type ID LPAREN parameters RPAREN SEMI_COLON
    '''
    print(f"Function Declaration: {p[3]} {p[2]}({', '.join(p[5])})")
def p_parameters(p):
    '''
    parameters : parameter
            | parameter COMMA parameters
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
def p_parameter(p):
    '''
    parameter : type ID
    '''
    p[0] = f"{p[1]} {p[2]}"
def p_type(p):
    '''
    type : INT_TYPE
        | FLOAT_TYPE
        | STRING_TYPE
        | VOID_TYPE
    '''
    p[0] = p[1]
def p_error(p):
    if p:
        print(f"Syntax error: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")
parser = yacc.yacc()
# Test the parser
data = '''
    public int Add(int x, int y);
    public void PrintName(string name);
    public float Subtract(float a, float b);
'''
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)