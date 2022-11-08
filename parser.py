# ------------------------------------------------------------
# parser.py
#
# parser for ALi language
# ------------------------------------------------------------
import ply.yacc as yacc

from lexer import tokens
from semantic_rules import semantics

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
    '''main : FUNC MAIN found_main_function '(' ')' '{' main_block '}' '''

def p_found_main_function(p):
    ''' found_main_function : '''
    semantics.found_main_function()

# ----------------------
# MAIN FUNCTION RULES 
def p_main_block(p):
    '''main_block : function_block start_function update_function'''

def p_start_function(p):
    '''start_function : VOID FUNC START '(' ')' '{' sft '}' '''

def p_update_function(p):
    '''update_function : VOID FUNC UPDATE '(' ')' interior_block '''

def p_sft(p):
    '''sft : gen_canvas stm
            | stm'''

def p_special_function_statement(p):
    '''special_function_statement : set_canvas_title
                                  | set_canvas_bg 
                                  | draw_game_object'''

# TODO: Add checks to make sure params are of the right type
def p_gen_canvas(p):
    '''gen_canvas : GEN_CANVAS '(' expression ',' expression ',' STRING_CONST ')' ';' '''

def p_set_canvas_title(p):
    '''set_canvas_title : SET_CANVAS_TITLE '(' STRING_CONST ')' ';' '''

def p_set_canvas_bg(p):
    '''set_canvas_bg : SET_CANVAS_BG '(' STRING_CONST ')' ';' '''

# Special getter functions will be treated as expressions 
def p_get_window_h(p):
    '''get_window_h : GET_WINDOW_H '(' ')' '''

def p_get_window_w(p):
    '''get_window_w : GET_WINDOW_W '(' ')' '''

def p_get_game_ev(p):
    '''get_game_ev : GET_GAME_EV '(' ')' '''

# TODO: Add checks to make sure params are of the right type
def p_draw_game_object(p):
    '''draw_game_object : DRAW_GAME_OBJECT '(' expression ',' expression ',' expression ',' expression ',' STRING_CONST ')' ';' '''

# ----------------------
# STATEMENTS RULES 

def p_function_block(p):
    '''function_block : vars stm
                        | stm '''

def p_stm(p):
    '''stm : statements stm_p '''

def p_stm_p(p):
    '''stm_p : stm
             | empty'''
             
def p_vars(p):
    '''vars : VAR ids ':' vars_types ';' store_ids vars_p'''

def p_vars_types(p):
    '''vars_types : type
                  | array_type'''

def p_vars_p(p):
    '''vars_p : vars
              | empty'''

def p_ids(p):
    '''ids : ID store_id ids_p'''

def p_store_id(p):
    '''store_id : '''
    semantics.add_id(p[-1])

def p_store_ids(p):
    '''store_ids : '''
    semantics.store_ids()

def p_ids_p(p):
    '''ids_p : ',' ids
             | empty'''

def p_type(p):
    '''type : INT set_current_type
            | FLOAT set_current_type
            | CHAR set_current_type
            | BOOL set_current_type '''
    p[0] = p[1]

def p_set_current_type(p):
    '''set_current_type : '''
    semantics.set_current_type(p[-1])

def p_array_type(p):
    '''array_type : ARRAY '<' type '>' array_indexing'''

def p_functions(p):
    '''functions : return_function functions
                 | void_function functions
                 | return_function
                 | void_function'''

def p_return_function(p):
    '''return_function : type FUNC ID store_function '(' p ')' '{' start_function_ic function_block end_function '}' '''

def p_p(p):
    '''p : params
         | empty'''

def p_void_function(p):
    '''void_function : VOID set_current_type FUNC ID store_function '(' p ')' '{' start_function_ic function_block end_function '}' '''

def p_store_function(p):
    '''store_function : '''
    semantics.store_function(p[-1])

def p_start_function_ic(p):
    '''start_function_ic : '''
    semantics.start_function()

def p_end_function(p):
    '''end_function : '''
    semantics.end_function()

def p_statements(p):
    # TODO: Handle return statement correctly
    '''statements : assignment ';'
                  | array_assignment
                  | call_to_fun ';'
                  | write
                  | conditionals
                  | cycles
                  | read
                  | special_function_statement
                  | RETURN expression ';' handle_return_statement '''

def p_handle_return_statement(p):
    '''
    handle_return_statement : 
    '''
    semantics.handle_return_statement()

def p_conditionals(p):
    '''conditionals : if_statement end_if
                    | if_else_statement end_if
                    | if_else_if_statement end_if '''

def p_if_statement(p):
    '''if_statement : simple_if_statement'''

def p_simple_if_statement(p):
    '''simple_if_statement : IF '(' expression ')' start_if  interior_block'''

def p_if_else_statement(p):
    '''if_else_statement : simple_if_statement simple_else_statement'''

def p_simple_else_statement(p):
    '''simple_else_statement : start_else ELSE interior_block'''

def p_if_else_if_statement(p):
    '''if_else_if_statement : simple_if_statement simple_else_if_statement simple_else_statement
                            | simple_if_statement simple_else_if_statement'''

def p_simple_else_if_statement(p):
    '''simple_else_if_statement : start_else ELIF '(' expression ')' start_if interior_block more_else_if_statement '''

def p_more_else_if_statement(p):
    '''more_else_if_statement : simple_else_if_statement
                              | empty'''

def p_start_if(p):
    '''start_if : '''
    semantics.if_start()

def p_start_else(p):
    '''start_else : '''
    semantics.else_start()

def p_end_if(p):
    '''end_if : '''
    semantics.end_if()

def p_interior_block(p):
    '''interior_block : '{' '}'
                      | '{' stm '}' '''

def p_params(p):
    '''params : ID ':' type ',' params
              | ID ':' type'''
    semantics.store_function_param(p[1], p[3])

def p_assignment(p):
    '''assignment : ID '=' add_op expression
                  | ID array_type '=' expression '''
    if len(p)-1 == 4:
        semantics.add_id_operand(p[1])
        semantics.gen_assignment_quad()


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
               | write_param '''

def p_write_param(p):
    '''write_param : STRING_CONST add_const_to_operand_stack_string print_value
                   | variable print_value'''

def p_print_value(p):
    '''
    print_value :
    '''
    semantics.print_value()

def p_read(p):
    '''read : READ '(' read_p ')' ';' '''
 
def p_read_p(p):
    '''read_p : STRING_CONST add_const_to_operand_stack_string read_constant ',' read_p
              | STRING_CONST add_const_to_operand_stack_string read_constant '''

def p_read_constant(p):
    '''
    read_constant :
    '''
    semantics.read_constant()

def p_call_to_fun(p):
    '''call_to_fun : ID verify_function '(' gen_activation_quad ')' verify_params_number end_function_call
                   | ID verify_function '(' gen_activation_quad call_p ')' verify_params_number end_function_call '''

def p_call_p(p):
    '''call_p : expression call_argument ',' move_to_next_param  call_p
              | expression call_argument '''

def p_verify_function(p):
    ''' verify_function : '''
    semantics.verify_function(p[-1])

def p_gen_activation_quad(p):
    ''' gen_activation_quad : '''
    semantics.gen_activation_record_quad()

def p_call_argument(p):
    ''' call_argument : '''
    semantics.call_argument()

def p_move_to_next_param(p):
    ''' move_to_next_param : '''
    semantics.move_to_next_param()

def p_verify_params_number(p):
    ''' verify_params_number : '''
    semantics.verify_params_number()

def p_end_function_call(p):
    ''' end_function_call : '''
    semantics.end_function_call()

def p_cycles(p):
    '''cycles : while
                | for'''

def p_array_indexing(p):
    '''array_indexing : '[' expression ']' 
                      | '[' expression ']'  '[' expression ']' '''

def p_while(p):
    '''while : WHILE start_while '(' expression ')' evaluate_while_expression interior_block end_while'''

def p_start_while(p):
    '''
    start_while :
    '''
    semantics.start_while()

def p_evaluate_while_expression(p):
    '''
    evaluate_while_expression :
    '''
    semantics.evaluate_while_expression()

def p_end_while(p):
    '''
    end_while :
    '''
    semantics.end_while()

def p_for(p):
    '''for : FOR '(' assignment ';' start_for expression ';' eval_for_expression assignment ')' interior_block end_for'''

def p_start_for(p):
    '''
    start_for :
    '''
    semantics.start_for()

def p_eval_for_expression(p):
    '''
    eval_for_expression :
    '''
    semantics.evaluate_for_expression()

def p_end_for(p):
    '''
    end_for :
    '''
    semantics.end_for()

# ----------------------
# EXRPESSIONS RULES 

def p_expression(p):
    '''expression : t_exp 
                  | t_exp OR add_op expression gen_operation'''

def p_t_exp(p):
    '''t_exp : g_exp 
             | g_exp AND add_op t_exp gen_operation'''

def p_g_exp(p):
    '''g_exp : m_exp 
          | m_exp op g_exp gen_operation
          | '!' add_op g_exp not_action'''

def p_not_action(p):
    '''
    not_action : 
    '''
    semantics.not_quad()

def p_op(p):
    '''op : '>' add_op
          | '<' add_op
          | GREATER_EQ add_op
          | LESS_EQ add_op
          | EQUAL add_op
          | DIFFERENT add_op'''

def p_m_exp(p):
    '''m_exp : term
           | m_exp '+' add_op term gen_operation
           | m_exp '-' add_op term gen_operation '''

def p_term(p):
    '''term : factor
            | term '*' add_op factor gen_operation
            | term '/' add_op factor gen_operation'''

def p_add_op(p):
    '''
    add_op :
    '''
    semantics.add_operator(p[-1])

def p_factor(p):
    '''factor : '(' expression ')'
              | constants '''

def p_constants(p):
    '''constants : I_CONST add_const_to_operand_stack_int
                 | F_CONST add_const_to_operand_stack_float
                 | C_CONST add_const_to_operand_stack_char
                 | TRUE add_const_to_operand_stack_bool
                 | FALSE add_const_to_operand_stack_bool
                 | variable
                 | call_to_fun
                 | get_window_h
                 | get_window_w
                 | get_game_ev'''

def p_variable(p):
    '''variable : ID array_indexing 
                | ID add_variable_to_operand_stack'''

def p_add_variable_to_operand_stack(p):
    '''add_variable_to_operand_stack : '''
    semantics.add_id_operand(p[-1])

def p_add_const_to_operand_stack_string(p):
    '''
    add_const_to_operand_stack_string : 
    '''
    semantics.add_constant_operand(p[-1], 'string')

def p_add_const_to_operand_stack_int(p):
    '''add_const_to_operand_stack_int : '''
    semantics.add_constant_operand(p[-1], 'int')

def p_add_const_to_operand_stack_float(p):
    '''add_const_to_operand_stack_float : '''
    semantics.add_constant_operand(p[-1], 'float')

def p_add_const_to_operand_stack_char(p):
    '''add_const_to_operand_stack_char : '''
    semantics.add_constant_operand(p[-1], 'char')

def p_gen_operation(p):
    ''' gen_operation : '''
    semantics.gen_operation_quad()

def p_add_const_to_operand_stack_bool(p):
    '''add_const_to_operand_stack_bool : '''
    semantics.add_constant_operand(p[-1], 'bool')


# ----------------------
# EMPTY & ERROR RULES 
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    err_string = f"Syntax error in input at line {p.lineno} at character {p.lexpos} unexpected \'{p.value}\' "
    raise Exception(err_string)

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
    print(semantics.id_queue)
    print(semantics.types_stack)
    print(semantics.operands_stack)
    print(semantics.operators_stack)
    print(semantics.function_directory)
    i = 1
    for quad in semantics.quadruples:
        print(f'{i}. {quad}')
        i += 1