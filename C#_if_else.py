# import ply.lex as lex
# import ply.yacc as yacc

# # Token list
# tokens = (
#     'ID',
#     'IF',
#     'LPAREN',
#     'RPAREN',
#     'LBRACE',
#     'RBRACE',
#     'SEMICOLON',  # Add SEMICOLON token
# )

# # Regular expressions for tokens
# t_IF = r'if'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
# t_SEMICOLON = r';'  # Regular expression for SEMICOLON token

# # Ignored characters
# t_ignore = ' \t'

# # Error handling
# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# # Parsing rules
# def p_start(p):
#     'start : statement'
#     p[0] = p[1]

# def p_statement_if(p):
#     'statement : IF LPAREN condition RPAREN LBRACE statements RBRACE'
#     p[0] = f'if ({p[3]})\n{{\n{p[6]}\n}}'

# def p_condition(p):
#     'condition : expression'
#     p[0] = p[1]

# def p_expression_id(p):
#     'expression : ID'
#     p[0] = p[1]

# def p_statements(p):
#     '''statements : statement SEMICOLON statements
#                 | statement'''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = p[1] + ';\n' + p[3] if p[3] else p[1]

# def p_statement_semicolon(p):
#     'statement : statement SEMICOLON'
#     p[0] = p[1] + ';'

# def p_error(p):
#     print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")

# # Build the lexer and parser
# lexer = lex.lex()
# parser = yacc.yacc()

# data='''
#     if(int i=0;i<n;i++)'''

# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)


import ply.lex as lex
import ply.yacc as yacc

# Token list
tokens = (
    'ID',
    'IF',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',  # Add SEMICOLON token
)

# Regular expressions for tokens
t_IF = r'if'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SEMICOLON = r';'  # Regular expression for SEMICOLON token

# Ignored characters
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Parsing rules
def p_start(p):
    'start : statement'
    p[0] = p[1]

def p_statement_if(p):
    'statement : IF LPAREN condition RPAREN LBRACE statements RBRACE'
    p[0] = f'if ({p[3]})\n{{\n{p[6]}\n}}'

def p_condition(p):
    'condition : expression'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_statements(p):
    '''statements : statement SEMICOLON statements
                | statement'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ';\n' + p[3] if p[3] else p[1]

def p_statement_semicolon(p):
    'statement : statement SEMICOLON'
    p[0] = p[1] + ';'

def p_error(p):
    print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

data='''
    if(int i=0;i<n;i++)'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)