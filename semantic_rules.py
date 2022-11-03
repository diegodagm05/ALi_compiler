from collections import deque

from quadruple import  Quadruple
from semantic_cube import SemanticCube, types, operations
from vars_table import VarsTable
from memory import virtual_memory
from func_dir import FuncDir

sem_cube = SemanticCube()
class SemanticRules:
    operands_stack = deque()
    operators_stack = deque()
    types_stack = deque()
    jump_stack = deque()
    id_queue = deque()
    quadruples : list[Quadruple] = []
    quadruple_counter = 1
    function_directory = FuncDir()
    current_scopeID : str
    current_var_table : VarsTable
    const_vars_table = VarsTable()
    current_param_count : int
    current_local_var_count : int
    current_temp_count : int


    def add_id(self, id: str) -> None:
        self.id_queue.append(id)

    # TODO: Change this function when handling array types
    def set_current_type(self, type: str) -> None:
        self.current_type = type

    def store_ids(self) -> None:
        self.current_local_var_count = 0
        while len(self.id_queue) > 0:
            name = self.id_queue.popleft()
            self.current_var_table.add_entry(name, self.current_type)
            self.current_local_var_count += 1
        self.store_number_of_local_variables()

    # Quadruple related modules
    def add_operator(self, operator: str) -> None:
        self.operators_stack.append(operator)

    def add_id_operand(self, operand) -> None:
        # TODO: We are using a "global" vars table right now, but this lookup must be done on the current scope when
        # we enable context switching
        # FIX TODO: `self.current_var_table` is being changed on self.set_scope
        variable = self.current_var_table.lookup_entry(operand)
        self.operands_stack.append(variable.address)
        self.types_stack.append(variable.type)

    def add_constant_operand(self, operand, type):
        # TODO: Assign memory correctly to constant values by storing them in the correct var table
        # First, check if the constant has already been declared, since we can reuse it
        (exists, constant) = self.const_vars_table.lookup_entry(operand)
        if exists:
            self.operands_stack.append(constant.address)
            self.types_stack.append(constant.type)
        else:    
            address = virtual_memory.assign_mem_address('CONST', False)
            self.const_vars_table.add_entry(operand, type)
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
            self.quadruples.append(quadruple)
            self.quadruple_counter += 1
            self.types_stack.append(match_types)
            self.operands_stack.append(temp_result)
            self.function_directory.increment_scope_num_temp_vars(self.current_scopeID, match_types)

    def gen_assignment_quad(self):
        assignment_operand_type = self.types_stack.pop()
        assign_result_type = self.types_stack.pop()
        assignment_operator = self.operators_stack.pop()
        match_types = sem_cube.match_types(assign_result_type, assignment_operand_type, assignment_operator)
        if match_types == 'ERROR':
            raise Exception(f'Type mismatch. \'{assignment_operand_type}\' cannot be assigned to \'{assign_result_type}')
        else:
            assign_result = self.operands_stack.pop()
            expression_to_assign = self.operands_stack.pop()
            quadruple = Quadruple(assignment_operator, expression_to_assign, result=assign_result)
            self.quadruples.append(quadruple)
            self.quadruple_counter += 1

    def if_start(self):
        expression_type = self.types_stack.pop()
        if expression_type != types['bool']:
            raise Exception('Type mismatch on conditional expression')
        else:
            result = self.operands_stack.pop()
            quadruple = Quadruple('gotof', result)
            self.quadruple_counter += 1
            self.quadruples.append(quadruple)
            self.jump_stack.append(self.quadruple_counter - 1)

    def else_start(self):
        quadruple = Quadruple('goto',-1)
        self.quadruple_counter += 1 
        self.quadruples.append(quadruple)
        false_jump = self.jump_stack.pop()
        self.jump_stack.append(self.quadruple_counter - 1)
        self.quadruples[false_jump-1].fill_result(self.quadruple_counter)


    def end_if(self):
        while len(self.jump_stack) > 0:
            pending_jump = self.jump_stack.pop()
            self.quadruples[pending_jump-1].fill_result(self.quadruple_counter)

    def start_while(self):
        self.jump_stack.append(self.quadruple_counter)

    def evaluate_while_expression(self):
        expression_type = self.types_stack.pop()
        if expression_type != types['bool']:
            raise Exception('Type mismatch on conditional expression')
        else:
            result = self.operands_stack.pop()
            quadruple = Quadruple('gotof', result)
            self.quadruple_counter += 1
            self.quadruples.append(quadruple)
            self.jump_stack.append(self.quadruple_counter - 1)
    
    def end_while(self):
        pending_jump = self.jump_stack.pop()
        return_to = self.jump_stack.pop()
        quadruple = Quadruple('goto', return_to)
        self.quadruples.append(quadruple)
        self.quadruple_counter += 1
        self.quadruples[pending_jump - 1].fill_result(self.quadruple_counter)

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
            # Change the current scope, and therefore current var table
            self.set_scope(name)
            self.current_param_count = self.current_local_var_count =  self.current_temp_count = 0

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
        self.function_directory.set_scope_num_vars(self.current_scopeID, self.current_local_var_count, self.current_type)

    def start_function(self):
        # Insert into Dir Function the current quad counter to establish where the function starts
        self.function_directory.set_scope_start(self.current_scopeID, self.quadruple_counter)

    def end_function(self):
        # Generate an END FUNC quadruple TODO: Handle release of function memory in runtime
        end_func_quad = Quadruple('endfunc')
        self.quadruple_counter += 1
        self.quadruples.append(end_func_quad)
        # TODO: Check if the function's return value type matches its return type
        

