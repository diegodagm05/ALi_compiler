types = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'bool': 'BOOL',
}

class Semantic_Cube():

    operators = (
        '+', '-', '*', '/', '&&', '||', '==', '!=', '>', '<', '>=', '<=',
    )

    semantic_cube = {
        'int': {
            'int': {
                '+': types['int'],
                '-': types['int'],
                '*': types['int'],
                '/': types['int'],
                '&&': types['bool'],
                '||': types['bool'],
                '==': types['bool'],
                '!=': types['bool'],
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
            },
            'float': {
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
            },
            'char': {
                '+': types['char'],
                '-': types['char'],
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            },
            'bool': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            }
        },
        'float': {
            'int': {
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
            },
            'float': {
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': types['bool'],
                '!=': types['bool'],
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
            },
            'char': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            },
            'bool': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            }
        },
        'char': {
            'int': {
                '+': types['char'],
                '-': types['char'],
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            },
            'float': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            },
            'char': {
                '+': types['char'],
                '-': types['char'],
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': types['char'],
                '!=': types['char'],
                '>': types['char'],
                '<': types['char'],
                '>=': types['char'],
                '<=': types['char'],
            },
            'bool': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            }
        },
        'bool': {
            'int': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            },
            'float': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            },
            'char': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            },
            'bool': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': types['bool'],
                '||': types['bool'],
                '==': types['bool'],
                '!=': types['bool'],
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
            }
        }
    }
   
    def match_types(self, type1: str, type2: str, operator: str) -> str:
        if type1 not in types or type1 not in types:
            raise Exception('Unknown type used')
        
        if operator not in self.operators:
            raise Exception('Unknown operator used')

        result = self.semantic_cube[type1][type2][operator]

        if result == 'ERROR':
            raise Exception(f'Type mismatch. \'{type1}\' cannot be combined with \'{type2}\' with the \'{operator}\' operator')
        
        return result