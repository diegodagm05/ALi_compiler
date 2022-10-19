from semantic_cube import types

# TODO: Grow this data structure as we add more to the variable table
class VarsTableEntry:
    def __init__(self, type: str) -> None:
        self.type = type

    

class VarsTable():
    vars_table = {}
    def add_entry(self, name: str, type: str) -> None:
        if type not in types:
            raise Exception('Unknown type used')
        if name in self.vars_table:
            raise Exception('Redeclaration of identifier is not allowed')
        # TODO: Figure out if we need to add more information when creating a new entry 
        self.vars_table[name] = VarsTableEntry(types[type])

    def lookup_entry(self, name: str) -> VarsTableEntry:
        if name not in self.vars_table:
            raise Exception('Undeclared identifier')

        return self.vars_table[name]