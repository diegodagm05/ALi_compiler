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

    def add_id(self, id: str) -> None:
        self.id_stack.append(id)

    # TODO: Change this function when handling array types
    def set_current_type(self, type: str) -> None:
        self.current_type = type

    def store_ids(self) -> None:
        while len(self.id_stack) > 0:
            name = self.id_stack.pop()
            print(f'Name: {name}')
            vars_table.add_entry(name, self.current_type)

    def add_operator(self, operator: str) -> None:
        self.operators_stack.append(operator)

    def add_operand(self, operand: int, operand_type: str) -> None:
        self.types_stack.append(operand_type)
        self.operands_stack.append(operand)


