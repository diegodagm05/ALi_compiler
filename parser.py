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
    '''g_vf : vars functions
            | vars
            | functions'''

def p_main(p):
    '''main : VOID FUNC MAIN '(' ')' '{' function_block '}' '''

# ----------------------
# STATEMENTS RULES 

def p_vars(p):
    '''vars : VAR ids ':' type ';' vars_p'''

def p_vars_p(p):
    '''vars_p : vars
              | empty'''

def p_stm(p):
    '''stm : statements stm_p '''

def p_stm_p(p):
    '''stm_p : stm
             | empty'''

def p_ids(p):
    '''ids : ID ids_p'''

def p_ids_p(p):
    '''ids_p : ',' ids
             | empty'''

def p_type(p):
    '''type : INT 
            | FLOAT
            | CHAR
            | BOOL
            | array_type'''

def p_array_type(p):
    '''array_type : ARRAY '[' expression ']'
                  | ARRAY '[' expression ']' '[' expression ']' '''

def p_functions(p):
    '''functions : return_function functions
                 | void_function functions
                 | return_function
                 | void_function'''

def p_function_block(p):
    '''function_block : vars stm
                        | stm '''

def p_return_function(p):
    '''return_function : type FUNC ID '(' p ')' '{' function_block RETURN ID ';' '}'
                       | type FUNC ID '(' p ')' '{' function_block RETURN expression ';' '}' '''

def p_p(p):
    '''p : params
         | empty'''

def p_void_function(p):
    '''void_function : VOID FUNC ID '(' p ')' '{' function_block '}' '''

def p_statements(p):
    '''statements : assignment
                  | array_assignment
                  | call_to_fun ';'
                  | write 
                  | conditionals
                  | cycles
                  | read'''

def p_conditionals(p):
    '''conditionals : IF '(' expression ')' interior_block cond_in_p ELSE interior_block'''

def p_cond_in_p(p):
    '''cond_in_p : cond_in
                 | empty'''

def p_cond_in(p):
    '''cond_in : ELSE IF '(' expression ')' interior_block cond_in
               | ELSE IF '(' expression ')' interior_block'''

def p_interior_block(p):
    '''interior_block : '{' '}'
                      | '{' stm '}' '''

def p_params(p):
    '''params : ID ':' type ',' params
              | ID ':' type'''

def p_assignment(p):
    '''assignment : ID '=' expression ';'
                  | ID array_type '=' expression'''

def p_array_assignment(p):
    '''array_assignment : ID '=' array_assign_type ';' '''
 
def p_array_assign_type(p): 
    '''array_assign_type : 1d_array_init
                         | 2d_array_init'''

def p_1d_array_init(p):
    '''1d_array_init : '[' exp_1d ']' '''

def p_exp_1d(p):
    '''exp_1d : expression ',' exp_1d
              | expression'''

def p_2d_array_init(p):
    '''2d_array_init : '[' exp_2d ']' '''

def p_exp_2d(p):
    '''exp_2d : 1d_array_init ',' exp_2d
              | 1d_array_init'''

def p_write(p):
    '''write : PRINT '(' write_p ')' ';' '''
 
def p_write_p(p):
    '''write_p : write_param ',' write_p 
               | write_param'''

def p_write_param(p):
    '''write_param : STRING_CONST
                   | ID'''

def p_read(p):
    '''read : READ '(' read_p ')' ';' '''
 
def p_read_p(p):
    '''read_p : STRING_CONST ',' read_p
              | STRING_CONST'''

def p_call_to_fun(p):
    '''call_to_fun : ID '(' ')'
                   | ID '(' call_p ')' '''
def p_call_p(p):
    '''call_p : expression ',' call_p
              | expression'''

def p_cycles(p):
    '''cycles : while
                | for'''

def p_array_indexing(p):
    '''array_indexing : ID '[' expression ']' 
                      | ID '[' expression ']'  '[' expression ']' '''

def p_while(p):
    '''while : WHILE '(' expression ')' interior_block'''

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
          | '!' exp'''

def p_op(p):
    '''op : '>'
          | '<'
          | GREATER_EQ
          | LESS_EQ
          | EQUAL
          | DIFFERENT'''

def p_exp(p):
    '''exp : term
           | term op_1 term'''

def p_op_1(p):
    '''op_1 : '+'
            | '-' '''

def p_term(p):
    '''term : factor
            | factor op_2 factor'''

def p_op_2(p):
    '''op_2 : '*'
            | '/' '''

def p_factor(p):
    '''factor : '(' expression ')'
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
    print(f"Syntax error in input at line {p.lineno}")
    raise Exception(p.type, p.value, p.lineno, p.lexpos)

parser = yacc.yacc(debug=True)

def test():
    print('Enter file name to be tested (with .al extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    parser.parse(input_str)
    print('Accepted code')

if __name__ == "__main__":
    test()