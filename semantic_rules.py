from collections import deque
from quadruple import  Quadruple
from semantic_cube import SemanticCube, types, operations
from vars_table import VarsTable
from memory import virtual_memory

vars_table = VarsTable()
sem_cube = SemanticCube()
class SemanticRules:
    operands_stack = deque()
    operators_stack = deque()
    types_stack = deque()
    jump_stack = deque()
    id_stack = deque()
    quadruples : list[Quadruple] = []
    quadruple_counter = 1

    def add_id(self, id: str) -> None:
        self.id_stack.append(id)

    # TODO: Change this function when handling array types
    def set_current_type(self, type: str) -> None:
        print(f'Setting current type {type}')
        self.current_type = type

    def store_ids(self) -> None:
        print(f'Storing ids {self.id_stack}')
        while len(self.id_stack) > 0:
            name = self.id_stack.pop()
            vars_table.add_entry(name, self.current_type)

    # Quadruple related modules
    def add_operator(self, operator: str) -> None:
        print(f'adding operator {operator}')
        self.operators_stack.append(operator)

    def add_id_operand(self, operand) -> None:
        # TODO: We are using a "global" vars table right now, but this lookup must be done on the current scope when
        # we enable context switching
        variable = vars_table.lookup_entry(operand)
        self.operands_stack.append(variable.address)
        self.types_stack.append(variable.type)

    def add_constant_operand(self, operand, type):
        # TODO: Assign memory correctly to constant values by storing them in the correct var table
        address = virtual_memory.assign_mem_address('CONST', False)
        # vars_table.add_entry(operand, type)
        self.operands_stack.append(address)
        self.types_stack.append(type)
                    
    def gen_operation_quad(self) -> None:
        right_type = self.types_stack.pop()
        left_type = self.types_stack.pop()
        curr_operator = self.operators_stack.pop()
        match_types = sem_cube.match_types(right_type, left_type, curr_operator)
        print('generating operation quad')
        if match_types == 'ERROR':
            raise Exception(f'Type mismatch. \'{left_type}\' cannot be combined with \'{right_type}\' with the \'{curr_operator}\' operator')
        else:
            right_operand = self.operands_stack.pop()
            left_operand = self.operands_stack.pop()
            temp_result = virtual_memory.assign_mem_address(match_types, is_temp=True)
            quadruple = Quadruple(curr_operator, left_operand, right_operand, temp_result)
            print(f'generated quadruple: {quadruple}')
            self.quadruples.append(quadruple)
            self.quadruple_counter += 1
            self.types_stack.append(match_types)
            self.operands_stack.append(temp_result)

    def gen_assignment_quad(self):
        assignment_operand_type = self.types_stack.pop()
        assign_result_type = self.types_stack.pop()
        
        match_types = sem_cube.match_types(assign_result_type, assignment_operand_type, '=')
        if match_types == 'ERROR':
            raise Exception(f'Type mismatch. \'{assignment_operand_type}\' cannot be assigned to \'{assign_result_type}')
        else:
            expression_to_assign = self.operands_stack.pop()
            assign_result = self.operands_stack.pop()
            quadruple = Quadruple('=', expression_to_assign, result=assign_result)
            self.quadruples.append(quadruple)
            self.quadruple_counter += 1


