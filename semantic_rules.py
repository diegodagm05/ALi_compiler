from collections import deque

from quadruple import  Quadruple
from semantic_cube import SemanticCube, types, operations
from vars_table import VarsTable, ConstVarsTable
from virtual_memory import virtual_memory
from func_dir import FuncDir

sem_cube = SemanticCube()

class CompilationResults:
    def __init__(self, func_dir: FuncDir, consts_table: ConstVarsTable, quadruples: list[Quadruple]) -> None:
        self.func_dir : FuncDir = func_dir
        self.consts_table : ConstVarsTable = consts_table
        self.quadruples : list[Quadruple] = quadruples

class SemanticRules:

    operands_stack = deque()
    operators_stack = deque()
    types_stack = deque()
    jump_stack = deque()
    id_queue = deque()
    is_array_queue = deque()
    dim_queue = deque()
    quadruples : list[Quadruple] = []
    quadruple_counter = 0
    function_directory = FuncDir()
    current_scopeID : str
    current_call_scopeID : str
    call_param_ptr : str
    call_scope_params_list : list[str]
    current_var_table : VarsTable
    const_vars_table : ConstVarsTable = ConstVarsTable()
    current_param_count : int = 0
    current_scope_var_count : int = 0
    current_temp_count : int = 0

    def __init__(self) -> None:
        self.set_scope('global')
        self.current_call_param_counter = 0
        # Goto main quad
        goto_main_quad = Quadruple('goto', 'main')
        self.append_quad(goto_main_quad)

    def append_quad(self, quadruple: Quadruple) -> None:
        self.quadruples.append(quadruple)
        self.quadruple_counter += 1

    def add_id(self, id: str, is_array: bool) -> None:
        self.id_queue.append(id)
        self.is_array_queue.append(is_array)
        # print(f'id_queue rn: {self.id_queue}')

    # TODO: Change this function when handling array types
    def set_current_type(self, type: str) -> None:
        self.current_type = type


    def set_dim1_size(self, dim: int):
        self.dim_queue.append(dim)
        self.dim_queue.append(1)
    
    def set_dim2_size(self, dim: int):
        self.dim_queue.pop()
        self.dim_queue.append(dim)        

    def store_ids(self) -> None:     
        self.current_local_var_count = 0
        dim1 = dim2 = total_size = 1
        while len(self.id_queue) > 0:
            name = self.id_queue.popleft()
            is_array = self.is_array_queue.popleft()
            if len(self.dim_queue) > 0:
                dim1 = self.dim_queue.popleft()
                dim2 = self.dim_queue.popleft()
                total_size = dim1 * dim2
            if self.current_scopeID == 'global':
              self.current_var_table.add_entry(name, self.current_type, True, is_array, dim1, dim2, total_size)
            else:
              self.current_var_table.add_entry(name, self.current_type, False, is_array, dim1, dim2, total_size)
            self.current_scope_var_count += 1
        self.store_number_of_local_variables()

    # Quadruple related modules
    def add_operator(self, operator: str) -> None:
        self.operators_stack.append(operator)

    def add_id_operand(self, operand) -> None:
        # First, look if the operand is the defined in the local scope
        (is_defined, variable) = self.current_var_table.lookup_entry(operand)
        if not is_defined:
            # if it is not in the local scope, look it up on the global scope
            global_var_table = self.function_directory.get_scope_var_table('global')
            (is_defined_glbally, global_variable) = global_var_table.lookup_entry(operand)
            if not is_defined_glbally:
                raise Exception(f'Undeclared identifier \'{operand}\'')
            else:
                self.operands_stack.append(global_variable.address)
                self.types_stack.append(global_variable.type)
        else:
            self.operands_stack.append(variable.address)
            self.types_stack.append(variable.type)

    def add_constant_operand(self, operand, type):
        # First, check if the constant has already been defined, since we can reuse it
        (is_defined, constant) = self.const_vars_table.lookup_entry(operand)
        if is_defined:
            self.operands_stack.append(constant.address)
            self.types_stack.append(constant.type)
        else:    
            address = self.const_vars_table.add_entry(operand, type)
            self.operands_stack.append(address)
            self.types_stack.append(type)
                    
    def gen_operation_quad(self) -> None:
        right_type = self.types_stack.pop()
        left_type = self.types_stack.pop()
        curr_operator = self.operators_stack.pop()
        match_types = sem_cube.match_types(right_type, left_type, curr_operator)
        if match_types == 'ERROR':
            raise Exception(f'Type mismatch. \'{left_type}\' cannot be combined with \'{right_type}\' with the \'{curr_operator}\' operator')
        else:
            right_operand = self.operands_stack.pop()
            left_operand = self.operands_stack.pop()
            temp_result = virtual_memory.assign_mem_address(match_types, is_temp=True)
            quadruple = Quadruple(curr_operator, left_operand, right_operand, temp_result)
            self.append_quad(quadruple)
            self.types_stack.append(match_types)
            self.operands_stack.append(temp_result)
            self.function_directory.increment_scope_num_temp_vars(self.current_scopeID, match_types)

    def gen_assignment_quad(self):
        assign_result_type = self.types_stack.pop()
        assignment_operand_type = self.types_stack.pop()
        assignment_operator = self.operators_stack.pop()
        match_types = sem_cube.match_types(assign_result_type, assignment_operand_type, assignment_operator)
        assign_result = self.operands_stack.pop()
        expression_to_assign = self.operands_stack.pop()
        if match_types == 'ERROR':
            raise Exception(f'Type mismatch. \'{assignment_operand_type}\' \' {expression_to_assign} \' cannot be assigned to \'{assign_result_type} \'{assign_result}\' \n''')
        else:
            quadruple = Quadruple(assignment_operator, expression_to_assign, result=assign_result)
            self.append_quad(quadruple)
    
    def not_quad(self):
        not_operator = self.operators_stack.pop()
        operand_type = self.types_stack.pop()
        if operand_type != types['bool']:
            raise Exception('Type Mismatch. \'!\' operator expects boolean type')
        operand = self.operands_stack.pop()
        temp_result = virtual_memory.assign_mem_address(operand_type, is_temp=True)
        quadruple = Quadruple(not_operator, operand, result= temp_result)
        self.append_quad(quadruple)
        self.types_stack.append(operand_type)
        self.operands_stack.append(temp_result)            
        self.function_directory.increment_scope_num_temp_vars(self.current_scopeID, operand_type)
     

    def if_start(self):
        expression_type = self.types_stack.pop()
        if expression_type != types['bool']:
            raise Exception('Type mismatch on conditional expression')
        else:
            result = self.operands_stack.pop()
            # Apend the gotof quad we are about to create
            self.jump_stack.append(self.quadruple_counter)
            quadruple = Quadruple('gotof', result)
            self.append_quad(quadruple)

    def else_start(self):
        false_jump = self.jump_stack.pop()
        # Append the goto quad we are about to create
        self.jump_stack.append(self.quadruple_counter)
        quadruple = Quadruple('goto',-1)
        self.append_quad(quadruple)
        # Fill the result of the false jump with the next quadruple we will create
        self.quadruples[false_jump].fill_result(self.quadruple_counter)


    def end_if(self):
        while len(self.jump_stack) > 0:
            pending_jump = self.jump_stack.pop()
            self.quadruples[pending_jump].fill_result(self.quadruple_counter)

    def start_while(self):
        self.jump_stack.append(self.quadruple_counter)

    def evaluate_while_expression(self):
        expression_type = self.types_stack.pop()
        if expression_type != types['bool']:
            raise Exception('Type mismatch on conditional expression')
        else:
            result = self.operands_stack.pop()
            self.jump_stack.append(self.quadruple_counter)
            quadruple = Quadruple('gotof', result)
            self.append_quad(quadruple)
    
    def end_while(self):
        pending_jump = self.jump_stack.pop()
        return_to = self.jump_stack.pop()
        quadruple = Quadruple('goto', result=return_to)
        self.append_quad(quadruple)
        self.quadruples[pending_jump].fill_result(self.quadruple_counter)

    def start_for(self):
        self.jump_stack.append(self.quadruple_counter)

    def evaluate_for_expression(self):
        expression_type = self.types_stack.pop()
        if expression_type != types['bool']:
            raise Exception('Type mismatch on conditional expression')
        else:
            result = self.operands_stack.pop()
            self.jump_stack.append(self.quadruple_counter)
            quadruple = Quadruple('gotof', result)
            self.append_quad(quadruple)

    def save_for_increment(self):
        self.for_increment_quad = self.quadruples[-1]
        del self.quadruples[-1]

    
    def end_for(self):
        self.append_quad(self.for_increment_quad)
        pending_jump = self.jump_stack.pop()
        return_to = self.jump_stack.pop()
        quadruple = Quadruple('goto', result=return_to)
        self.append_quad(quadruple)
        self.quadruples[pending_jump].fill_result(self.quadruple_counter)
    
    def print_value(self):
        result = self.operands_stack.pop()
        self.types_stack.pop()
        quadruple = Quadruple('print', None, None, result)
        self.append_quad(quadruple)

    def read_constant(self):
        result = self.operands_stack.pop()
        self.types_stack.pop()
        quadruple = Quadruple('read', None, None, result)
        self.quadruples.append(quadruple)

    def set_scope(self, scopeID: str):
        self.current_var_table = self.function_directory.get_scope_var_table(scopeID)
        self.current_scopeID = scopeID

    # Function declaration rules
    def store_function(self, name: str):
        # Insert function name into dir function table, add its type, while veryfing that there is no other function with the same name
        if name in self.function_directory.get_func_dir():
            raise Exception(f'Function with name {name} has already been declared.')
        else:
            self.function_directory.create_scope(name, self.current_type)
            # if the function returns a value, store it as a global variable
            if self.current_type != 'void':
                self.set_scope('global')
                self.current_var_table.add_entry(name, self.current_type, is_global_entry=True)
                self.function_directory.increment_scope_num_vars('global', 1, self.current_type)
            # Change the current scope, and therefore current var table
            self.set_scope(name)
            self.current_param_count = self.current_scope_var_count =  self.current_temp_count = 0

    def store_function_param(self, paramName: str, paramType: str):
        # Insert parameter into the current var table (local scope) with type
        if paramType not in types:
            raise Exception(f'Unknown parameter type {paramType} for {paramName}')
        else:
            self.current_var_table.add_entry(paramName, paramType)
            self.current_param_count += 1
            self.function_directory.add_to_param_list(self.current_scopeID, paramType)

    def store_number_of_local_variables(self):
        # Save the number of local variables for the function on the Dir Function table
        self.function_directory.increment_scope_num_vars(self.current_scopeID, self.current_scope_var_count, self.current_type)

    def start_function(self):
        # Insert into Dir Function the current quad counter to establish where the function starts
        self.function_directory.set_scope_start(self.current_scopeID, self.quadruple_counter)

    def end_function(self):
        # Check if the function's return value type matches its return typen value type matches its return type
        current_scope = self.function_directory.get_scope(self.current_scopeID)
        if current_scope.type != 'void' and not current_scope.is_returning_value:
            raise Exception(f'Function \'{self.current_scopeID}()\' defined with a \'{current_scope.type}\' return type but there are no return statements in the function definition.')
        # Generate an END FUNC quadruple TODO: Handle release of function memory in runtime
        end_func_quad = Quadruple('endfunc')
        self.append_quad(end_func_quad)
        # Release scope vars table and reset virtual memory
        current_scope.release_scope_vars_table()
        virtual_memory.reset_scope_counters()
    
    def found_main_function(self):
        self.function_directory.get_scope('main').starts_at = self.quadruple_counter
        self.quadruples[0].fill_result(self.quadruple_counter)
        self.set_scope('main')

    def end_main_function(self):
        # TODO: Remove comments when finished with arrays
        # self.function_directory.get_scope('main').release_scope_vars_table()
        end_program_quad = Quadruple('endprogram')
        self.append_quad(end_program_quad)

    def handle_return_statement(self):
        current_scope = self.function_directory.get_scope(self.current_scopeID)
        if self.current_scopeID == 'main':
            raise Exception('Return statement not allowed in main function.')
        elif current_scope.type == 'void':
            raise Exception('Void function is not allowed to return a value.')
        else:
            return_type = self.types_stack.pop()
            if return_type != current_scope.type:
                raise Exception(f'Returning a \'{return_type}\' expression in \'{self.current_scopeID}()\' which is signed as \'{current_scope.type}\' function.')
            else:
                return_value = self.operands_stack.pop()
                (current_scope_global_var_exists,  current_scope_global_var) = self.function_directory.get_scope('global').vars_table.lookup_entry(self.current_scopeID)
                if not current_scope_global_var_exists: 
                    raise Exception(f'Unable to find a return address for function \'{self.current_scopeID}()\'')
                return_quad = Quadruple('return',return_value, result=current_scope_global_var.address)
                self.append_quad(return_quad)
                self.function_directory.set_is_returning_value(self.current_scopeID, True)


    # Function calling rules
    def verify_function(self, name):
        if name not in self.function_directory.get_func_dir():
            raise Exception(f'Undeclared function {name}.')
        else: 
            self.current_call_scopeID = name
            global_scope_var_table = self.function_directory.get_scope_var_table('global')
            (does_function_return_value, func_as_var) = global_scope_var_table.lookup_entry(name)
            if does_function_return_value:
                self.operands_stack.append(func_as_var.address)
                self.types_stack.append(func_as_var.type)


    def gen_activation_record_quad(self):
        scope = self.function_directory.get_scope(self.current_call_scopeID)
        # resources needed will be stored as a list
        resources = [
            [scope.num_vars_int, scope.num_vars_float, scope.num_vars_char, scope.num_vars_bool],
            [scope.num_temps_int, scope.num_temps_float, scope.num_temps_char, scope.num_temps_bool]
        ]
        for param in scope.params_list:
            if param == 'i':
                resources[0][0] += 1
            elif param == 'f':
                resources[0][1] += 1
            elif param == 'c':
                resources[0][2] += 1
            elif param == 'b':
                resources[0][3] += 1
        era_quad = Quadruple('era', result=resources)
        self.append_quad(era_quad)
        self.call_scope_params_list = scope.params_list
        self.current_call_param_counter = 0
        if len(self.call_scope_params_list) > 0:
            self.set_call_param_ptr()

    def call_argument(self):
        argument = self.operands_stack.pop()
        argument_type = self.types_stack.pop()
        if self.call_param_ptr != types[argument_type]:
            raise Exception(f'Type mismatch. \n Parameter {self.current_call_param_counter} of function {self.current_call_scopeID} is of type {self.call_param_ptr} and is being passed an expression of type {argument_type}')
        else:
            # Reverse engineer the virtual address that was given to the parameter on its local var table
            # This will make generating an activation record with the params a whole lot easier
            current_call_scope = self.function_directory.get_scope(self.current_call_scopeID)
            curent_param_type_indicator = current_call_scope.params_list[self.current_call_param_counter]
            param_vaddr = self.current_call_param_counter
            if curent_param_type_indicator == 'i':
                param_vaddr += virtual_memory.local_int_range[0]
            elif curent_param_type_indicator == 'f':
                param_vaddr += virtual_memory.local_float_range[0]
            elif curent_param_type_indicator == 'c':
                param_vaddr += virtual_memory.local_char_range[0]
            param_quad = Quadruple('parameter', argument, 'param' + str(self.current_call_param_counter), result=param_vaddr)
            self.append_quad(param_quad)
            self.current_call_param_counter += 1

    def move_to_next_param(self):
        self.set_call_param_ptr()

    def verify_params_number(self):
        if self.current_call_param_counter > len(self.call_scope_params_list):
            raise Exception(f'Too many arguments. Function \'{self.current_call_scopeID}\' expects {len(self.call_scope_params_list)} arguments and got {self.current_call_param_counter}.')
        elif self.current_call_param_counter < len(self.call_scope_params_list):
            raise Exception(f'Too few arguments. Function \'{self.current_call_scopeID}\' expects {len(self.call_scope_params_list)} arguments and got {self.current_call_param_counter}..')

    def end_function_call(self):
        call_scope = self.function_directory.get_scope(self.current_call_scopeID)
        end_function_quad = Quadruple('gosub', self.current_call_scopeID, result=call_scope.starts_at)
        self.append_quad(end_function_quad)
        if call_scope.type != 'void':
            temp_result = virtual_memory.assign_mem_address(call_scope.type, is_temp=True)
            (call_scope_exists, current_call_scope_global_entry) = self.function_directory.get_scope_var_table('global').lookup_entry(self.current_call_scopeID)
            if not call_scope_exists:
                raise Exception(f'\'{self.current_call_scopeID}\' is unable to return a value')
            assign_call_result_quad = Quadruple('=', current_call_scope_global_entry.address, result=temp_result)
            self.append_quad(assign_call_result_quad)
            self.operands_stack.append(temp_result)
            self.types_stack.append(call_scope.type)
            self.function_directory.increment_scope_num_temp_vars(self.current_scopeID, call_scope.type)

    def set_call_param_ptr(self) -> str:
        param_type = self.call_scope_params_list[self.current_call_param_counter]
        if  param_type == 'i':
            self.call_param_ptr = types['int']
        elif param_type == 'f':
            self.call_param_ptr = types['float']
        elif param_type == 'c':
            self.call_param_ptr = types['char']
        elif param_type == 'b':
            self.call_param_ptr = types['bool']

    def get_compilation_results(self) -> CompilationResults:
        results = CompilationResults(self.function_directory, self.const_vars_table, self.quadruples)
        return results
      

semantics = SemanticRules()