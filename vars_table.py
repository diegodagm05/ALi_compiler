from typing import Union
from semantic_cube import types
from virtual_memory import virtual_memory

# TODO: Grow this data structure as we add more to the variable table
class VarsTableEntry:
    def __init__(self, type: str, address: int, is_array: bool = False, dim1: int = 1, dim2: int = 1, total_dim_size: int = 1) -> None:
        self.type = type
        self.address = address
        self.is_array = is_array
        self.dim1 = dim1
        self.dim2 = dim2
        self.total_dim_size = total_dim_size

    def __str__(self) -> str:
        return f'type: {self.type} address: {self.address} is_array: {self.is_array} dim1: {self.dim1} dim2: {self.dim2} total_size: {self.total_dim_size}'

    def __repr__(self) -> str:
        return f'type: {self.type} address: {self.address} is_array: {self.is_array} dim1: {self.dim1} dim2: {self.dim2} total_size: {self.total_dim_size}'

class VarsTable():
    def __init__(self) -> None:
        self.vars_table = {}
    def __str__(self) -> str:
        return str(self.vars_table)

    def add_entry(self, name: str, type: str, is_global_entry: bool = False, is_array: bool = False, dim1: int = 1, dim2: int = 1, total_size: int = 1) -> None:
        if type not in types:
            raise Exception(f'Unknown type used {type}')
        if name in self.vars_table:
            raise Exception(f'Redeclaration of identifier {name} is not allowed')
        if is_array:
            # print(f'The name of this array is {name} ')
            address = virtual_memory.assign_array_address(types[type], total_size, is_global_entry)
            self.vars_table[name] = VarsTableEntry(types[type], address, is_array, dim1, dim2, total_size)
        else:
            address = virtual_memory.assign_mem_address(types[type])
            self.vars_table[name] = VarsTableEntry(types[type], address)

    def lookup_entry(self, name: str) -> tuple[bool, Union[VarsTableEntry, None]]:
        if name not in self.vars_table:
            return (False, None)
        return (True, self.vars_table[name])

class ConstVarsTable():
    def __init__(self) -> None:
        # Our first constants will be boolean literals true and false
        address1 = virtual_memory.assign_mem_address(types['bool'], is_const=True)
        address2 = virtual_memory.assign_mem_address(types['bool'], is_const=True)
        self.const_vars_table = {
            'true': VarsTableEntry(types['bool'], address1),
            'false': VarsTableEntry(types['bool'], address2)
        }
    def __str__(self) -> str:
        return str(self.const_vars_table)

    def add_entry(self, name: str, type: str) -> int:
        if type == 'string':
            address = virtual_memory.assign_constant_address_string()
        else:
            if type not in types:
                raise Exception(f'Unknown type used {type}')
            if name in self.const_vars_table:
                raise Exception(f'Redeclaration of identifier {name} is not allowed')
            address = virtual_memory.assign_mem_address(types[type], is_const=True)
            self.const_vars_table[name] = VarsTableEntry(types[type], address)
        return address

    def lookup_entry(self, name: str) -> tuple[bool, Union[VarsTableEntry, None]]:
        if name not in self.const_vars_table:
            return (False, None)
        return (True, self.const_vars_table[name])