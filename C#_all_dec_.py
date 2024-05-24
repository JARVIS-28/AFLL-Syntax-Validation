# # SIMPLE DATATYPE DECLARATION
# import ply.lex as lex
# import ply.yacc as yacc

# # Lex code
# tokens = (
#     'ID',
#     'COLON',
#     'SEMICOLON',
#     'INT_TYPE',
#     'FLOAT_TYPE',
#     'STRING_TYPE',
# )
# t_SEMICOLON=r';'
# t_COLON= r':'
# t_INT_TYPE = r'\d+'
# t_FLOAT_TYPE = r'\d+\.\d+'
# t_STRING_TYPE = r'"[^"]*"'

# t_ignore = ' \t\n'

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     return t

# # def t_COLON(t):
# #     r':'
# #     return t
# # def t_INT_TYPE(t):
# #     r'int'
# #     return t
# # def t_FLOAT_TYPE(t):
# #     r'float'
# #     return t
# # def t_STRING_TYPE(t):
# #     r'string'
# #     return t

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Yacc code
# def p_declaration(p):
#     '''
#     declaration : type ID SEMICOLON
#     '''
#     print(f"Declaration: {p[2]} is of type {p[1]}")

# def p_type(p):
#     '''
#     type : INT_TYPE
#             | FLOAT_TYPE
#             | STRING_TYPE
#     '''
#     p[0] = p[1]

# def p_error(p):
#     print("Syntax error")

# parser = yacc.yacc()

# # Test the parser
# data='''
    
#     string w;
#     float x;
#     int q;
# '''
# lexer.input(data)
# # for token in lexer:
# #     print(token)

# # parser.parse(data)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)



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
#     # 'COLON',
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
# # t_COLON= r':'
# t_SEMI_COLON=r';'
# t_INT_TYPE = r'\d+'
# t_FLOAT_TYPE = r'\d+\.\d+'
# # t_STRING_TYPE = r'"[^"]*"'
# t_STRING_TYPE= r'string'
# t_VOID_TYPE=r'void'

# t_ignore = ' \t\n'

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     return t

# # def t_LPAREN(t):
# #     r'\('
# #     return t

# # def t_RPAREN(t):
# #     r'\)'
# #     return t

# # def t_LBRACKET(t):
# #     r'\['
# #     return t

# # def t_RBRACKET(t):
# #     r'\]'
# #     return t

# # def t_COLON(t):
# #     r':'
# #     return t

# # def t_INT_TYPE(t):
# #     r'int'
# #     return t

# # def t_FLOAT_TYPE(t):
# #     r'float'
# #     return t

# # def t_STRING_TYPE(t):
# #     r'string'
# #     return t

# # def t_VOID_TYPE(t):
# #     r'void'
# #     return t

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Yacc code
# def p_declaration(p):
#     # '''
#     # declaration : variable_declaration
#     #             | array_declaration
#     # '''
#     '''
#     declaration : array_declaration'''
#     print("Declaration:", p[1])

# # def p_variable_declaration(p):
# #     '''
# #     variable_declaration : ID COLON type
# #     '''
# #     p[0] = f"Variable '{p[1]}' of type {p[3]}"

# def p_array_declaration(p):
#     # '''
#     # array_declaration : ID LBRACKET INT_TYPE RBRACKET COLON type
#     # '''
#     '''
#     array_declaration : type LBRACKET type RBRACKET ID SEMI_COLON'''
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
    
    
    

# # FUNCTION DECLARATION
# import ply.lex as lex
# import ply.yacc as yacc

# # Lex code
# tokens = (
#     'ID',
#     'LPAREN',
#     'RPAREN',
#     'COMMA',
#     'SEMI_COLON',
#     'INT_TYPE',
#     'FLOAT_TYPE',
#     'STRING_TYPE',
#     'VOID_TYPE',
#     'PUBLIC',
# )

# t_LPAREN= r'\('
# t_RPAREN= r'\)'
# t_COMMA= r','
# t_SEMI_COLON=r';'
# t_INT_TYPE = r'\d+'
# t_FLOAT_TYPE = r'\d+\.\d+'
# t_STRING_TYPE = r'"[^"]*"'
# t_VOID_TYPE=r'void'
# t_PUBLIC=r'public'

# t_ignore = ' \t\n'

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     return t

# # def t_LPAREN(t):
# #     r'\('
# #     return t

# # def t_RPAREN(t):
# #     r'\)'
# #     return t

# # def t_COMMA(t):
# #     r','
# #     return t

# # def t_INT_TYPE(t):
# #     r'int'
# #     return t

# # def t_FLOAT_TYPE(t):
# #     r'float'
# #     return t

# # def t_STRING_TYPE(t):
# #     r'string'
# #     return t

# # def t_VOID_TYPE(t):
# #     r'void'
# #     return t

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Yacc code
# def p_function_declaration(p):
#     '''
#     function_declaration : PUBLIC type ID LPAREN parameters RPAREN SEMI_COLON
#     '''
#     print(f"Function Declaration: {p[3]} {p[2]}({', '.join(p[5])})")
# def p_parameters(p):
#     '''
#     parameters : parameter
#             | parameter COMMA parameters
#     '''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = [p[1]] + p[3]
# def p_parameter(p):
#     '''
#     parameter : type ID
#     '''
#     p[0] = f"{p[1]} {p[2]}"
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
# data = '''
#     public int Add(int x, int y);
#     public void PrintName(string name);
#     public float Subtract(float a, float b);
# '''
# lexer.input(data)
# # for token in lexer:
# #     print(token)
# # parser.parse(data, lexer=lexer)
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)



# #FOR LOOP
# import ply.lex as lex
# import ply.yacc as yacc

# # Lex code
# tokens = (
#     'ID',
#     'LPAREN',
#     'RPAREN',
#     'SEMI_COLON',
#     'INT_TYPE',
#     'EQUALS',
#     'LESS_THAN',
#     'PLUS',
#     'MINUS',
#     'NUMBER',
#     'FOR',
# )

# t_LPAREN= r'\('
# t_RPAREN= r'\)'
# t_SEMI_COLON=r';'
# t_PLUS=r'\+'
# t_MINUS=r'\-'
# t_EQUALS=r'='
# t_LESS_THAN=r'<'
# t_NUMBER=r'\d+'
# t_INT_TYPE = r'\d+'
# t_FOR=r'for'

# t_ignore=r' \t\n'

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     return t

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # Parser rules
# def p_statement(p):
#     '''
#     statement : for_loop
#     '''
#     print("Statement:", p[1])

# def p_for_loop(p):
#     '''
#     for_loop : FOR LPAREN initialization SEMI_COLON condition SEMI_COLON increment RPAREN
#     '''
#     p[0] = f"For loop with initialization: {p[3]}, condition: {p[5]}, and increment: {p[7]}"

# def p_initialization(p):
#     '''
#     initialization : INT_TYPE ID EQUALS NUMBER
#     '''
#     p[0] = f"Initialize {p[2]} with {p[4]}"

# def p_condition(p):
#     '''
#     condition : ID LESS_THAN NUMBER
#     '''
#     p[0] = f"Check if {p[1]} is less than {p[3]}"

# def p_increment(p):
#     '''
#     increment : ID PLUS PLUS
#             | ID MINUS MINUS
#     '''
#     p[0] = f"Increment {p[1]}"

# def p_error(p):
#     if p:
#         print(f"Syntax error: Unexpected token '{p.value}'")
#     else:
#         print("Syntax error at EOF")

# parser = yacc.yacc()

# # data = '''
# #     for (int i = 0; i < 10; i++)
# #     {
# #         // Do something
# #     }
# # '''

# data='''
#     for(int i=0;i<n;i++)'''

# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)