from typing import Union
from semantic_cube import operations

quadruple_operations = operations | {
    'print': 14,
    'read': 15,
    'goto': 16,
    'gotot': 17,
    'gotof': 18,
    'gosub': 19,
    'was': 20,
    'parameter': 21,
    'endfunc': 22,
    'return': 23, 
}

class Quadruple():
    # Note that operators and result are memory addresses
    # None on result is for quadruples that may be generated with a pending result or quadruples that have no result
    def __init__(self, operation: str, operator1: int = -1, operator2: int = -1, result: Union[int, str] = None) -> None:
        if operation not in quadruple_operations:
            raise Exception('Unkown operation on quadruple')
        self.op_code = quadruple_operations[operation]
        self.operator1 = operator1
        self.operator2 = operator2
        self.result = result

    def __str__(self) -> str:
        return f'{self.op_code} {self.operator1} {self.operator2} {self.result}\n'

    def __repr__(self) -> str:
        return f'{self.op_code} {self.operator1} {self.operator2} {self.result}\n'

    def fill_result(self, result: int) -> None:
        self.result = result
    