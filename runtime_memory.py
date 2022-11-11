from collections import deque
from typing import Any, Union
from quadruple import Quadruple, quadruple_operations
from virtual_memory import VirtualMemory

class RunttimeMemory():
    def __init__(self, num_ints: int, num_floats: int, num_chars: int, num_bools: int, is_const_data_segment: bool = False) -> None:
        super().__init__()
        self.ints_mem : list[Union[int, None]] = self.generate_mem_segment(num_ints)
        self.floats_mem : list[Union[float, None]] = self.generate_mem_segment(num_floats)
        self.chars_mem : list[ Union[str, None]] = self.generate_mem_segment(num_chars)
        self.bools_mem : list[Union[bool, None]] = self.generate_mem_segment(num_bools)
        if is_const_data_segment:
            # TODO: Figure out how we can allocate specific memory for strings
            self.strings_mem : list[Union[str, None]] = self.generate_mem_segment(100)

    def generate_mem_segment(self, list_size: int):
        return [None] * list_size

    def retrieve_content(self, virtual_address: int) -> Any:
        int_index = self.get_int_index(virtual_address)
        float_index = self.get_float_index(virtual_address)
        char_index = self.get_char_index(virtual_address)
        bool_index = self.get_bool_index(virtual_address)
        string_index = self.get_string_index(virtual_address)
        if int_index != None: 
            return self.ints_mem[int_index]
        elif float_index != None: 
            return self.floats_mem[float_index]
        elif char_index != None: 
            return self.chars_mem[char_index]
        elif bool_index != None: 
            return self.bools_mem[bool_index]
        elif string_index != None: 
            return self.strings_mem[string_index]
        else:
            raise RuntimeError(f'Unable to access specified virtual address \'{virtual_address}\'')

    def assign_content(self, virtual_address: int, value: Any) -> None:
        int_index = self.get_int_index(virtual_address)
        float_index = self.get_float_index(virtual_address)
        char_index = self.get_char_index(virtual_address)
        bool_index = self.get_bool_index(virtual_address)
        string_index = self.get_string_index(virtual_address)
        if int_index != None:
            self.ints_mem[int_index] = value
        elif float_index != None: 
            self.floats_mem[float_index] = value
        elif char_index != None: 
            self.chars_mem[char_index] = value
        elif bool_index != None: 
            self.bools_mem[bool_index] = value
        elif string_index != None:
            self.strings_mem[string_index] = value
        else:
            raise RuntimeError(f'Unable to access specified virtual address \'{virtual_address}\'')

    def get_int_index(self, virtual_address: int) -> Union[int, None]:
        # Check if the address belongs to global ints
        if self.in_virtual_range(virtual_address, VirtualMemory.global_int_range[0], VirtualMemory.global_int_range[1]): 
            return virtual_address - VirtualMemory.global_bool_range[0]
        # Check if the address belongs to constant ints
        elif self.in_virtual_range(virtual_address, VirtualMemory.constant_int_range[0], VirtualMemory.constant_int_range[1]): 
            return virtual_address - VirtualMemory.constant_int_range[0]
        # Check if the address belongs to local ints
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_int_range[0], VirtualMemory.local_int_range[1]): 
            return virtual_address - VirtualMemory.local_int_range[0]
        # Check if the address belongs to temporal ints
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_int_range[0], VirtualMemory.local_int_range[1]):
            return virtual_address - VirtualMemory.temp_int_range[0]
        else: 
            return None

    def get_float_index(self, virtual_address: int) -> Union[float, None]:
        # Check if the address belongs to global floats
        if self.in_virtual_range(virtual_address, VirtualMemory.global_float_range[0], VirtualMemory.global_float_range[1]): 
            return virtual_address - VirtualMemory.global_bool_range[0]
        # Check if the address belongs to constant floats
        elif self.in_virtual_range(virtual_address, VirtualMemory.constant_float_range[0], VirtualMemory.constant_float_range[1]): 
            return virtual_address - VirtualMemory.constant_float_range[0]
        # Check if the address belongs to local floats
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_float_range[0], VirtualMemory.local_float_range[1]): 
            return virtual_address - VirtualMemory.local_float_range[0]
        # Check if the address belongs to temporal floats
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_float_range[0], VirtualMemory.local_float_range[1]):
            return virtual_address - VirtualMemory.temp_float_range[0]
        else: 
            return None

    def get_char_index(self, virtual_address: int) -> Union[str, None]:
        # Check if the address belongs to global ints
        if self.in_virtual_range(virtual_address, VirtualMemory.global_char_range[0], VirtualMemory.global_char_range[1]): 
            return virtual_address - VirtualMemory.global_bool_range[0]
        # Check if the address belongs to constant chars
        elif self.in_virtual_range(virtual_address, VirtualMemory.constant_char_range[0], VirtualMemory.constant_char_range[1]): 
            return virtual_address - VirtualMemory.constant_char_range[0]
        # Check if the address belongs to local chars
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_char_range[0], VirtualMemory.local_char_range[1]): 
            return virtual_address - VirtualMemory.local_char_range[0]
        # Check if the address belongs to temporal chars
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_char_range[0], VirtualMemory.local_char_range[1]):
            return virtual_address - VirtualMemory.temp_char_range[0]
        else: 
            return None

    def get_bool_index(self, virtual_address: int) -> Union[bool, None]:
        # Check if the address belongs to global bools
        if self.in_virtual_range(virtual_address, VirtualMemory.global_bool_range[0], VirtualMemory.global_bool_range[1]): 
            return virtual_address - VirtualMemory.global_bool_range[0]
        # Check if the address belongs to constant bools
        elif self.in_virtual_range(virtual_address, VirtualMemory.constant_bool_range[0], VirtualMemory.constant_bool_range[1]): 
            return virtual_address - VirtualMemory.constant_bool_range[0]
        # Check if the address belongs to local bools
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_bool_range[0], VirtualMemory.local_bool_range[1]): 
            return virtual_address - VirtualMemory.local_bool_range[0]
        # Check if the address belongs to temporal bools
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_bool_range[0], VirtualMemory.local_bool_range[1]):
            return virtual_address - VirtualMemory.temp_bool_range[0]
        else: 
            return None

    def get_string_index(self, virtual_address: int) -> Union[str, None]:
        # Check if the address belongs to constant strings
        if self.in_virtual_range(virtual_address, VirtualMemory.constant_string_range[0], VirtualMemory.constant_string_range[1]): 
            return virtual_address - VirtualMemory.constant_string_range[0]
        else: 
            return None
            
    def in_virtual_range(self, virtual_address: int, range_start: int, range_end: int):
        return virtual_address > range_start and virtual_address < range_end



