from collections import deque
from typing import Any, Union
from func_dir import FuncDir
from quadruple import Quadruple, quadruple_operations
from vars_table import ConstVarsTable
from virtual_memory import VirtualMemory

'''
MemorySegment class
Instantiating a MemorySegment object, we should now how many spaces we need for each datatype segment. Every memory segment has different lists that hold a specific type. 
These lists are created only on an as needed basis.
'''
class MemorySegment():
    def __init__(self, num_ints: int = 0, num_floats: int = 0, num_chars: int = 0, num_bools: int = 0, 
                num_ints_temp: int = 0, num_floats_temp: int = 0, num_chars_temp: int = 0, num_bools_temp: int = 0,
                num_temps_pointer: int = 0,
                num_strings: int = 0) -> None:
        # We check if we actually need to create the segment of memory for a given type
        if num_ints > 0:
            self.ints_mem : list[Union[int, None]] = self.generate_mem_segment(num_ints)
        if num_floats > 0:
            self.floats_mem : list[Union[float, None]] = self.generate_mem_segment(num_floats)
        if num_chars > 0:
            self.chars_mem : list[ Union[str, None]] = self.generate_mem_segment(num_chars)
        if num_bools > 0:
            self.bools_mem : list[Union[bool, None]] = self.generate_mem_segment(num_bools)
        if num_ints_temp > 0:
            self.ints_mem_temp : list[Union[int, None]] = self.generate_mem_segment(num_ints_temp)
        if num_floats_temp > 0:
            self.floats_mem_temp : list[Union[float, None]] = self.generate_mem_segment(num_floats_temp)
        if num_chars_temp > 0:
            self.chars_mem_temp : list[ Union[str, None]] = self.generate_mem_segment(num_chars_temp)
        if num_bools_temp > 0:
            self.bools_mem_temp : list[Union[bool, None]] = self.generate_mem_segment(num_bools_temp)
        if num_temps_pointer > 0:
            self.temps_pointer_mem : list[Union[int, None]] = self.generate_mem_segment(num_temps_pointer)
        if num_strings > 0:
            self.strings_mem : list[Union[str, None]] = self.generate_mem_segment(num_strings)

    def __repr__(self) -> str:
        result = ""
        if hasattr(self, 'ints_mem'):
            result += '\n Ints mem: ' + str(self.ints_mem)
        if hasattr(self, 'floats_mem'):
            result += '\n floats mem: ' + str(self.floats_mem)
        if hasattr(self, 'chars_mem'):
            result += '\n chars mem: ' + str(self.chars_mem)
        if hasattr(self, 'bools_mem'):
            result += '\n bools mem: ' + str(self.bools_mem)
        if hasattr(self, 'ints_mem_temp'):
            result += '\n Ints mem_temp: ' + str(self.ints_mem_temp)
        if hasattr(self, 'floats_mem_temp'):
            result += '\n floats mem_temp: ' + str(self.floats_mem_temp)
        if hasattr(self, 'chars_mem_temp'):
            result += '\n chars mem_temp: ' + str(self.chars_mem_temp)
        if hasattr(self, 'bools_mem_temp'):
            result += '\n bools mem_temp: ' + str(self.bools_mem_temp)
        if hasattr(self, 'temps_pointer_mem'):
            result += ' \n Temps pointer mem: ' +  str(self.temps_pointer_mem)
        if hasattr(self, 'strings_mem'):
            result += ' \n Strings mem: ' +  str(self.strings_mem)
        return result
            

    # This is a helper function to assign a memory segment of size list_size, where our underlying implementation of a memory segment is a list
    def generate_mem_segment(self, list_size: int):
        return [None] * list_size

    def retrieve_content(self, virtual_address: int) -> Any:
        int_index = self.get_int_index(virtual_address)
        int_temp_index = self.get_int_temp_index(virtual_address)
        float_index = self.get_float_index(virtual_address)
        float_temp_index = self.get_float_temp_index(virtual_address)
        char_index = self.get_char_index(virtual_address)
        char_temp_index = self.get_char_temp_index(virtual_address)
        bool_index = self.get_bool_index(virtual_address)
        bool_temp_index = self.get_bool_temp_index(virtual_address)
        temp_pointer_index = self.get_temp_pointer_index(virtual_address)
        string_index = self.get_string_index(virtual_address)
        if int_index != None: 
            value = self.ints_mem[int_index]
        elif int_temp_index != None:
            value = self.ints_mem_temp[int_temp_index]
        elif float_index != None: 
            value = self.floats_mem[float_index]
        elif float_temp_index != None:
            value = self.floats_mem_temp[float_temp_index]
        elif char_index != None: 
            value = self.chars_mem[char_index]
        elif char_temp_index != None: 
            value = self.chars_mem_temp[char_temp_index]
        elif bool_index != None: 
            value = self.bools_mem[bool_index]
        elif bool_temp_index != None: 
            value = self.bools_mem_temp[bool_temp_index]
        elif string_index != None: 
            value : str = self.strings_mem[string_index]
            value = value.replace("\"", '')
        elif temp_pointer_index != None:
            # Recursively calls this same function to retrieve the content from the "real" address the temp pointer is pointing to
            real_address = self.temps_pointer_mem[temp_pointer_index]
            value = self.retrieve_content(real_address)
        else:
            value = None

        if value is None:
            raise RuntimeError('Cannot use uninitialized variable.')
        else:
            return value

    '''
    assign_content method
    This method has a flag parameter to know if it is storing a virtual address. This is helpful when processing quadruples that reference a 
    temporal pointer address.
    '''
    def assign_content(self, virtual_address: int, value: Any, storing_vaddress: bool = False) -> None:
        int_index = self.get_int_index(virtual_address)
        int_temp_index = self.get_int_temp_index(virtual_address)
        float_index = self.get_float_index(virtual_address)
        float_temp_index = self.get_float_temp_index(virtual_address)
        char_index = self.get_char_index(virtual_address)
        char_temp_index = self.get_char_temp_index(virtual_address)
        bool_index = self.get_bool_index(virtual_address)
        bool_temp_index = self.get_bool_temp_index(virtual_address)
        temp_pointer_index = self.get_temp_pointer_index(virtual_address)
        string_index = self.get_string_index(virtual_address)
        if int_index != None: 
            self.ints_mem[int_index] = value
        elif int_temp_index != None:
            self.ints_mem_temp[int_temp_index] = value
        elif float_index != None: 
            self.floats_mem[float_index] = value
        elif float_temp_index != None:
            self.floats_mem_temp[float_temp_index] = value
        elif char_index != None: 
            self.chars_mem[char_index] = value
        elif char_temp_index != None: 
            self.chars_mem_temp[char_temp_index] = value
        elif bool_index != None: 
            self.bools_mem[bool_index] = value
        elif bool_temp_index != None: 
            self.bools_mem_temp[bool_temp_index] = value
        elif temp_pointer_index != None:
            # Test if we are storing a a virtual address using a temp pointer
            if storing_vaddress:
                self.temps_pointer_mem[temp_pointer_index] = value
            else:
                # If not, recursively calls this same function to retrieve the content from the "real" address the temp pointer is pointing to
                real_address = self.temps_pointer_mem[temp_pointer_index]
                self.assign_content(real_address, value)
        elif string_index != None: 
            self.strings_mem[string_index] = value
        else:
            raise RuntimeError(f'Unable to access specified virtual address \'{virtual_address}\'')

    '''
    The following methods (get_datatype_index) test whether the virtual address given is part of the range for the datatype and kind of address. 
    If it is, it returns the index by substracting the starting point of the virtual address for its specific datype and kind.
    If not, it returns None so that we know that the given virtual address is not part of the range
    '''

    def get_int_index(self, virtual_address: int) -> Union[int, None]:
        # Check if the address belongs to global ints
        if self.in_virtual_range(virtual_address, VirtualMemory.global_int_range[0], VirtualMemory.global_int_range[1]): 
            return virtual_address - VirtualMemory.global_int_range[0]
        # Check if the address belongs to constant ints
        elif self.in_virtual_range(virtual_address, VirtualMemory.constant_int_range[0], VirtualMemory.constant_int_range[1]): 
            return virtual_address - VirtualMemory.constant_int_range[0]
        # Check if the address belongs to local ints
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_int_range[0], VirtualMemory.local_int_range[1]): 
            return virtual_address - VirtualMemory.local_int_range[0]
        else: 
            return None
    def get_int_temp_index(self, virtual_address: int) -> Union[int, None]:
        if self.in_virtual_range(virtual_address, VirtualMemory.temp_int_range[0], VirtualMemory.temp_int_range[1]):
            return virtual_address - VirtualMemory.temp_int_range[0]
        else: 
            return None

    def get_float_index(self, virtual_address: int) -> Union[float, None]:
        # Check if the address belongs to global floats
        if self.in_virtual_range(virtual_address, VirtualMemory.global_float_range[0], VirtualMemory.global_float_range[1]): 
            return virtual_address - VirtualMemory.global_float_range[0]
        # Check if the address belongs to constant floats
        elif self.in_virtual_range(virtual_address, VirtualMemory.constant_float_range[0], VirtualMemory.constant_float_range[1]): 
            return virtual_address - VirtualMemory.constant_float_range[0]
        # Check if the address belongs to local floats
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_float_range[0], VirtualMemory.local_float_range[1]): 
            return virtual_address - VirtualMemory.local_float_range[0]
        else: 
            return None

    def get_float_temp_index(self, virtual_address: int) -> Union[float, None]:
        # Check if the address belongs to temporal floats
        if self.in_virtual_range(virtual_address, VirtualMemory.temp_float_range[0], VirtualMemory.temp_float_range[1]):
            return virtual_address - VirtualMemory.temp_float_range[0]
        else: 
            return None

    def get_char_index(self, virtual_address: int) -> Union[str, None]:
        # Check if the address belongs to global ints
        if self.in_virtual_range(virtual_address, VirtualMemory.global_char_range[0], VirtualMemory.global_char_range[1]): 
            return virtual_address - VirtualMemory.global_char_range[0]
        # Check if the address belongs to constant chars
        elif self.in_virtual_range(virtual_address, VirtualMemory.constant_char_range[0], VirtualMemory.constant_char_range[1]): 
            return virtual_address - VirtualMemory.constant_char_range[0]
        # Check if the address belongs to local chars
        elif self.in_virtual_range(virtual_address, VirtualMemory.local_char_range[0], VirtualMemory.local_char_range[1]): 
            return virtual_address - VirtualMemory.local_char_range[0]
        else: 
            return None
    
    def get_char_temp_index(self, virtual_address: int) -> Union[str, None]:
        # Check if the address belongs to temporal chars
        if self.in_virtual_range(virtual_address, VirtualMemory.temp_char_range[0], VirtualMemory.temp_char_range[1]):
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
        else: 
            return None
    
    def get_bool_temp_index(self, virtual_address: int) -> Union[bool, None]:
        # Check if the address belongs to temporal bools
        if self.in_virtual_range(virtual_address, VirtualMemory.temp_bool_range[0], VirtualMemory.temp_bool_range[1]):
            return virtual_address - VirtualMemory.temp_bool_range[0]
        else: 
            return None

    def get_temp_pointer_index(self, virtual_address: int) -> Union[str, None]:
        # Check if the address belongs to temp pointers
        if self.in_virtual_range(virtual_address, VirtualMemory.temp_pointer_range[0], VirtualMemory.temp_pointer_range[1]): 
            return virtual_address - VirtualMemory.temp_pointer_range[0]
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

'''

'''
class RuntimeMemory():
    def __init__(self, consts_table: ConstVarsTable, func_dir: FuncDir) -> None:
        # Build the constant memory segment
        self.constant_memory_segment : MemorySegment = self.generate_constant_memory_segment(consts_table)
        global_scope = func_dir.get_scope('global')
        # Build the global memory segment
        self.global_memory_segment : MemorySegment = MemorySegment(
            global_scope.num_vars_int,
            global_scope.num_vars_float,
            global_scope.num_vars_char,
            global_scope.num_vars_bool,
            num_temps_pointer=global_scope.num_pointer_temps
        )
        self.mem_stack : deque[MemorySegment] = deque()
        # Take advantage of the function directory to build out the main memory segment and set it as the current memory segment from the start
        self.current_mem_segment : MemorySegment = self.generate_main_memory_segment(func_dir)
        self.activation_record : MemorySegment = None

    def generate_constant_memory_segment(self, consts_table: ConstVarsTable) -> MemorySegment:
        mem_segment = MemorySegment(
            consts_table.types_counter['int'], 
            consts_table.types_counter['float'], 
            consts_table.types_counter['char'],
            consts_table.types_counter['bool'],
            num_strings=consts_table.types_counter['string']
        )
        # We use the constants table to build out the memory segment, using the keys as the values to be stored in memory 
        for value, const_entry in consts_table.const_vars_table.items():
            value_in_memory = value
            if value == 'true':
                value_in_memory = True
            elif value == 'false':
                value_in_memory = False
            mem_segment.assign_content(const_entry.address, value_in_memory)
                
        return mem_segment

    def generate_main_memory_segment(self, func_dir: FuncDir) -> MemorySegment:
        main_scope = func_dir.get_scope('main')
        mem_segment = MemorySegment(
            main_scope.num_vars_int,
            main_scope.num_vars_float,
            main_scope.num_vars_char,
            main_scope.num_vars_bool,
            main_scope.num_temps_int,
            main_scope.num_temps_float,
            main_scope.num_temps_char,
            main_scope.num_temps_bool,
            main_scope.num_pointer_temps
        )
        return mem_segment

    def create_mem_segment(self, resources: list[list[int]]) -> None:
        local_resources = resources[0]
        temp_resources = resources[1]
        temp_pointer_resources = resources[2]
        new_mem_segment = MemorySegment(local_resources[0], local_resources[1], local_resources[2], local_resources[3],temp_resources[0], temp_resources[1], temp_resources[2], temp_resources[3], temp_pointer_resources)
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

    '''
    The following are helper methods do determine from which memory segment we should retreive content from or assign content to. 
    We need to know if we should access the global, constant or current memory segment. 
    '''
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
