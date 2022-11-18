from typing import Union
from semantic_cube import operations

quadruple_operations = operations | {
    'print': 14,
    'endprint': 15,
    'read': 16,
    'goto': 17,
    'gotot': 18,
    'gotof': 19,
    'gosub': 20,
    'era': 21,
    'parameter': 22,
    'endfunc': 23,
    'return': 24, 
    'verify': 25,
    'add_base_address': 26,
    'multiply_displacement': 27,
    'endprogram': 28
}

class Quadruple():
    # Note that operators and result are memory addresses
    # None on result is for quadruples that may be generated with a pending result or quadruples that have no result
    def __init__(self, operation: str, operator1: int = -1, operator2: int = -1, result: Union[int, str, list[int]] = None) -> None:
        if operation not in quadruple_operations:
            raise Exception('Unkown operation on quadruple')
        self.op_code = quadruple_operations[operation]
        self.operator1 = operator1
        self.operator2 = operator2
        self.result = result

    def __str__(self) -> str:
        return f'{self.op_code} {self.operator1} {self.operator2} {self.result}'

    def __repr__(self) -> str:
        return f'{self.op_code} {self.operator1} {self.operator2} {self.result}'

    def fill_result(self, result: int) -> None:
        if self.result is None:
            self.result = result
    