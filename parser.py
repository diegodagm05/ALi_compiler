# ------------------------------------------------------------
# parser.py
#
# parser for ALi language
# ------------------------------------------------------------
import ply.yacc as yacc

from lexer import tokens

# ----------------------
# GLOBAL RULES 
def p_program(p):
    '''program : global_vars_funs main
               | main'''

def p_global_vars_funs(p):
    '''global_vars_funs : g_vf''' 

def p_g_vf(p):
    '''g_vf : g_vars g_functions
            | g_vars
            | g_functions'''

def p_g_vars(p):
    '''g_vars : vars g_vars
              | vars'''

def p_g_functions(p):
    '''g_functions : functions g_functions
                   | functions'''

def p_main(p):
    '''main : VOID FUNC MAIN ( ) { vars s }
            | VOID FUNC MAIN ( ) { }'''

# ----------------------
# STATEMENTS RULES 

def p_vars(p):
    '''vars : VAR ids : type ; vars
            | VAR ids : type ;'''

def p_s(p):
    '''s : statements s
         | statements'''

def p_ids(p):
    '''ids : ID , ids
           | ID'''

def p_type(p):
    '''type : INT 
            | FLOAT
            | CHAR
            | BOOL
            | array_type'''

def p_array_type(p):
    '''array_type : ARRAY [ expression ]
                  | ARRAY [ expression ] [ expression ]'''

def p_functions(p):
    '''functions : return_function functions
                 | void_function functions
                 | return_function
                 | void_function'''

def p_return_function(p):
    '''return_function : type FUNC ID ( p ) { content RETURN ret }'''

def p_p(p):
    '''p : params
         | empty'''

def p_content(p):
    '''content : vars s
               | empty'''

def p_ret(p):
    '''ret : ID
           | expression'''

def p_void_function(p):
    '''void_function : VOID FUNC ID ( p ) { content }'''

def p_statements(p):
    '''statements : assigment
                  | call_to_fun ;
                  | write
                  | conditionals
                  | cycles
                  | read'''

def p_conditionals(p):
    '''conditionals : IF ( expression ) interior_block cond_in_p ELSE interior_block'''

def p_cond_in_p(p):
    '''cond_in_p : cond_in
                 | empty'''

def p_cond_in(p):
    '''cond_in : ELSE IF ( expression ) interior_block cond_in
               | ELSE IF ( expression ) interior_block'''

def p_interior_block(p):
    '''interior_block : { }
                      | { s }'''

def p_params(p):
    '''params : ID : type , params
              | ID : type'''

def p_assignment(p):
    '''assignment : ID = expression ;
                  | ID array_type = expression'''

def p_write(p):
    '''write : PRINT ( write_p ) ;'''

def p_write_p(p):
    '''write_p : write_param , write_p 
               | write_param'''

def p_write_param(p):
    '''write_param : STRING_CONST
                   | ID'''

def p_read(p):
    '''read : READ ( read_p ) ;'''

def p_read_p(p):
    '''read_p : STRING_CONST , read_p
              | STRING_CONST'''

def p_call_to_fun(p):
    '''call_to_fun : ID ( )
                   | ID ( call_p )'''
def p_call_p(p):
    '''call_p : expression , call_p
              | expression'''

def p_cycles(p):
    '''cycles : while
                | for'''

def p_array_indexing(p):
    '''array_indexing : ID [ expression ]
                      | ID [ expression ] [ expression ]'''

def p_while(p):
    '''while : WHILE ( expression ) interior_block'''

def p_for(p):
    '''for : FOR assignment UNTIL expression interior_block'''

# ----------------------
# EXRPESSIONS RULES 

def p_expression(p):
    '''expression : expression_p '''

def p_expression_p(p):
    '''expression_p : ex
                    | ex AND expression_p
                    | ex OR expression_p'''

def p_ex(p):
    '''ex : exp
          | exp op exp
          | ! exp'''

def p_op(p):
    '''op : >
          | <
          | GREATER_EQ
          | LESS_EQ
          | EQUAL
          | DIFFERENT'''

def p_exp(p):
    '''exp : term
           | term op_1 term'''

def p_op_1(p):
    '''op_1 : +
            | -'''

def p_term(p):
    '''term : factor
            | factor op_2 factor'''

def p_op_2(p):
    '''op_2 : *
            | /'''

def p_factor(p):
    '''factor : ( expression ) 
              | ID
              | array_indexing
              | call_to_fun
              | constants'''

def p_constants(p):
    '''constants : I_CONST
                 | F_CONST
                 | C_CONST'''

# ----------------------
# EMPTY & ERROR RULES 
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    raise Exception(p)

parser = yacc.yacc()