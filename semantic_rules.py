from collections import deque
from quadruple import  Quadruple
from semantic_cube import SemanticCube, types, operations
from vars_table import VarsTable

vars_table = VarsTable()

class SemanticRules:
    operands_stack = deque()
    operators_stack = deque()
    types_stack = deque()
    jump_stack = deque()
    id_stack = deque()
    quadruples : list[Quadruple]

    def __init__(self) -> None:
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

    def add_operand(self, operand: int, operand_type: str) -> None:
        self.types_stack.append(operand_type)
        self.operands_stack.append(operand)

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
        self.quadruples[pending_jump].fill_result(self.quadruple_counter)