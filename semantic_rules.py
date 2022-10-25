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
    quadruples : list[Quadruple]

    def _init_(self) -> None:
        self.quadruples = []
        self.quadruple_counter = 1

    def add_id(self, id: str) -> None:
        self.id_stack.append(id)

    # TODO: Change this function when handling array types
    def set_current_type(self, type: str) -> None:
        self.current_type = type

    def store_ids(self) -> None:
        while len(self.id_stack) > 0:
            name = self.id_stack.pop()
            vars_table.add_entry(name, self.current_type)

    # Quadruple related modules
    def add_operator(self, operator: str) -> None:
        self.operators_stack.append(operator)

    def add_id_operand(self, operand) -> None:
        # TODO: We are using a "global" vars table right now, but this lookup must be done on the current scope when
        # we enable context switching
        variable = vars_table.lookup_entry(operand)
        self.operands_stack.append(variable.address)
        self.types_stack.append(variable.type)

    def add_constant_operand(self, operand, type):
        self.operands_stack.append(operand)
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

    def gen_assignment_quad(self, id: str):
        assignment_operand_type = self.types_stack.pop()
        id_to_assign = vars_table.lookup_entry(id)
        match_types = sem_cube.match_types(id_to_assign.type, assignment_operand_type, '=')
        if match_types == 'ERROR':
            raise Exception(f'Type mismatch. \'{assignment_operand_type}\' cannot be assigned to \'{id_to_assign.type}')
        else:
            expression_to_assign = self.operands_stack.pop()
            quadruple = Quadruple('=', expression_to_assign, result=id_to_assign.address)
            self.quadruples.append(quadruple)
            self.quadruple_counter += 1


