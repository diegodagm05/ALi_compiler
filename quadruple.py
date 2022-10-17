from semantic_cube import operations

class Quadruple():
    # Note that operators and result are memory addresses
    def __init__(self, op_code: int, operator1: int, operator2: int, result: int) -> None:
        if op_code not in operations:
            raise Exception('Unkown operation on quadruple')
        self.op_code = op_code
        self.operator1 = operator1
        self.operator2 = operator2
        self.result = result
    