from collections import deque
from typing import Any, Union
from func_dir import FuncDir
from quadruple import Quadruple, quadruple_operations
from vars_table import ConstVarsTable
from virtual_memory import VirtualMemory

class MemorySegment():
    '''
    Instantiating a MemorySegment object, we should now how many spaces we need for each datatype segment. We also need to now if the
    object instantiated will be used to store constants, and therefero we need a segment for string constants.
    '''
    def __init__(self, num_ints: int, num_floats: int, num_chars: int, num_bools: int, num_strings: int = 0) -> None:
        super().__init__()
        self.ints_mem : list[Union[int, None]] = self.generate_mem_segment(num_ints)
        self.floats_mem : list[Union[float, None]] = self.generate_mem_segment(num_floats)
        self.chars_mem : list[ Union[str, None]] = self.generate_mem_segment(num_chars)
        self.bools_mem : list[Union[bool, None]] = self.generate_mem_segment(num_bools)
        if num_strings > 0: # TODO: This same check may make all memory segments more efficient, as we may not need to search through segments that do not exist!
            self.strings_mem : list[Union[str, None]] = self.generate_mem_segment(num_strings)

    def __repr__(self) -> str:
        if hasattr(self, 'strings_mem'):
            return 'Ints memory: ' + str(self.ints_mem) + '\n Floats mem: ' + str(self.floats_mem) + ' \n Chars mem: ' + str(self.chars_mem) + ' \n Bools mem: ' + str(self.bools_mem) + ' \n Strings mem: ' +  str(self.strings_mem)
        else:
            return 'Ints memory: ' + str(self.ints_mem) + '\n Floats mem: ' + str(self.floats_mem) + ' \n Chars mem: ' + str(self.chars_mem) + ' \n Bools mem: ' + str(self.bools_mem)
            

    # This is a helper function to assign a memory segment of size list_size, where our underlying implementation of a memory segment is a list
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
            return None

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

    '''
    The following four methods (get_datatype_index) test whether the virtual address given is part of the range for the datatype and kind of address. 
    If it is, it returns the index by substracting the starting point of the virtual address for its specific datype and kind.
    If not, it returns None so that we know that the given virtual address is not part of the range
    '''

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
        elif self.in_virtual_range(virtual_address, VirtualMemory.temp_int_range[0], VirtualMemory.temp_int_range[1]):
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
        elif self.in_virtual_range(virtual_address, VirtualMemory.temp_float_range[0], VirtualMemory.temp_float_range[1]):
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
        elif self.in_virtual_range(virtual_address, VirtualMemory.temp_char_range[0], VirtualMemory.temp_char_range[1]):
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
        elif self.in_virtual_range(virtual_address, VirtualMemory.temp_bool_range[0], VirtualMemory.temp_bool_range[1]):
            return virtual_address - VirtualMemory.temp_bool_range[0]
        else: 
            return None

    def get_string_index(self, virtual_address: int) -> Union[str, None]:
        # Check if the address belongs to constant strings
        if self.in_virtual_range(virtual_address, VirtualMemory.constant_string_range[0], VirtualMemory.constant_string_range[1]): 
            return virtual_address - VirtualMemory.constant_string_range[0]
        else: 
            return None
            
    # Helper function to test for a range
    def in_virtual_range(self, virtual_address: int, range_start: int, range_end: int):
        return virtual_address >= range_start and virtual_address <= range_end



class RuntimeMemory():
    def __init__(self, consts_table: ConstVarsTable, func_dir: FuncDir) -> None:
        self.constant_memory_segment : MemorySegment = self.generate_constant_memory_segment(consts_table)
        global_scope = func_dir.get_scope('global')
        self.global_memory_segment : MemorySegment = MemorySegment(
            global_scope.num_vars_int,
            global_scope.num_vars_float,
            global_scope.num_vars_char,
            global_scope.num_vars_bool
        )
        self.mem_stack : deque[MemorySegment] = deque()
        self.current_mem_segment : MemorySegment = self.generate_main_memory_segment(func_dir)
        self.activation_record : MemorySegment = None

    def generate_constant_memory_segment(self, consts_table: ConstVarsTable) -> MemorySegment:
        mem_segment = MemorySegment(
            consts_table.types_counter['int'], 
            consts_table.types_counter['float'], 
            consts_table.types_counter['char'],
            consts_table.types_counter['bool'],
            consts_table.types_counter['string']
        )
        for value, const_entry in consts_table.const_vars_table.items():
            mem_segment.assign_content(const_entry.address, value)
        return mem_segment

    def generate_main_memory_segment(self, func_dir: FuncDir) -> MemorySegment:
        main_scope = func_dir.get_scope('main')
        mem_segment = MemorySegment(
            main_scope.num_vars_int + main_scope.num_temps_int,
            main_scope.num_vars_float + main_scope.num_temps_float,
            main_scope.num_vars_char + main_scope.num_temps_char,
            main_scope.num_vars_bool + main_scope.num_temps_bool
        )
        return mem_segment

    def create_mem_segment(self, resources: list[int]) -> None:
        new_mem_segment = MemorySegment(resources[0], resources[1], resources[2], resources[3])
        self.activation_record = new_mem_segment

    def sleep_current_memory(self):
        self.mem_stack.append(self.current_mem_segment)
        self.current_mem_segment = self.activation_record
    
    def destroy_current_mem_segment(self) -> None:
        # When we are finished with a memory segment, we dispose of it and reset to what we had waiting in the stack
        del self.current_mem_segment
        self.current_mem_segment = self.mem_stack.pop()

    def retrieve_content(self, virtual_address: int):
        # see if we will retrieve it from the global memory segment
        if self.check_for_global_segment(virtual_address):
            return self.global_memory_segment.retrieve_content(virtual_address)
        elif self.check_for_constant_segment(virtual_address):
            return self.constant_memory_segment.retrieve_content(virtual_address)
        else:
            return self.current_mem_segment.retrieve_content(virtual_address)
    
    def assign_content(self, virtual_address: int, value: Any):
        # see if we will assign it to the global memory segment
        if self.check_for_global_segment(virtual_address):
            return self.global_memory_segment.assign_content(virtual_address, value)
        elif self.check_for_constant_segment(virtual_address):
            return self.constant_memory_segment.assign_content(virtual_address, value)
        else:
            return self.current_mem_segment.assign_content(virtual_address, value)

    def check_for_global_segment(self, virtual_address: int) -> bool:
        if ((virtual_address >= VirtualMemory.global_int_range[0] and virtual_address <= VirtualMemory.global_int_range[1])
            or (virtual_address >= VirtualMemory.global_float_range[0] and virtual_address <= VirtualMemory.global_float_range[1])
            or (virtual_address >= VirtualMemory.global_char_range[0] and virtual_address <= VirtualMemory.global_char_range[1])
            or (virtual_address >= VirtualMemory.global_bool_range[0] and virtual_address <= VirtualMemory.global_bool_range[1])):
            return True
    
    def check_for_constant_segment(self, virtual_address: int) -> bool:
        if ((virtual_address >= VirtualMemory.constant_int_range[0] and virtual_address <= VirtualMemory.constant_int_range[1])
            or (virtual_address >= VirtualMemory.constant_float_range[0] and virtual_address <= VirtualMemory.constant_float_range[1])
            or (virtual_address >= VirtualMemory.constant_char_range[0] and virtual_address <= VirtualMemory.constant_char_range[1])
            or (virtual_address >= VirtualMemory.constant_bool_range[0] and virtual_address <= VirtualMemory.constant_bool_range[1])
            or (virtual_address >= VirtualMemory.constant_string_range[0] and virtual_address <= VirtualMemory.constant_string_range[1])):
            return True
