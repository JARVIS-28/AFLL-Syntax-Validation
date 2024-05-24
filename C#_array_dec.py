# # ARRAY DECLARATION
# import ply.lex as lex
# import ply.yacc as yacc

# # Lex code
# tokens = (
#     'ID',
#     'LPAREN',
#     'RPAREN',
#     'LBRACKET',
#     'RBRACKET',
#     'SEMI_COLON',
#     'INT_TYPE',
#     'FLOAT_TYPE',
#     'STRING_TYPE',
#     'VOID_TYPE',
# )

# t_LPAREN= r'\('
# t_RPAREN= r'\)'
# t_LBRACKET=r'\['
# t_RBRACKET=r'\]'    
# t_SEMI_COLON=r';'
# # t_INT_TYPE = r'\d+'
# # t_FLOAT_TYPE = r'\d+\.\d+'
# # t_STRING_TYPE = r'"[^"]*"'
# t_INT_TYPE = r'int'
# t_FLOAT_TYPE = r'float'
# t_STRING_TYPE = r'string'
# t_VOID_TYPE=r'void'

# t_ignore = ' \t\n'

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     return t

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Yacc code
# def p_declaration(p):
#     '''
#     declaration : array_declaration
#     '''
#     print("Declaration:", p[1])

# def p_array_declaration(p):
#     '''
#     array_declaration : type LBRACKET type RBRACKET ID SEMI_COLON
#     '''
#     p[0] = f"Array '{p[5]}' of type {p[1]}"

# def p_type(p):
#     '''
#     type : INT_TYPE
#         | FLOAT_TYPE
#         | STRING_TYPE
#         | VOID_TYPE
#     '''
#     p[0] = p[1]

# def p_error(p):
#     if p:
#         print(f"Syntax error: Unexpected token '{p.value}'")
#     else:
#         print("Syntax error at EOF")

# parser = yacc.yacc()

# # Test the parser
# # data = '''
# #     x: int
# #     y: float
# #     z: string
# #     a[5]: int
# #     b[10]: float
    
# # '''
# data_1='''
#     string[] cars;
#     int[] x;
#     float[] qw;
#     flaot[] 1:
# '''
# lexer.input(data_1)
# # for token in lexer:
# #     print(token)

# # parser.parse(data_1)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)
    
