from semantic_cube import types

DATATYPE_SIZES = 16000
DATATYPE_KIND_SIZE = DATATYPE_SIZES // 4 # We use 4 because we have global, constant, local and temporal datatypes that we need to track
INT_START = 0
FLOAT_START = INT_START + DATATYPE_SIZES
CHAR_START = FLOAT_START + DATATYPE_SIZES
BOOL_START = CHAR_START + DATATYPE_SIZES
STRING_START = BOOL_START + DATATYPE_SIZES

class VirtualMemory():
    # Int ranges
    global_int_range = [INT_START, INT_START + DATATYPE_KIND_SIZE - 1]
    global_int_counter = global_int_range[0] 
    constant_int_range = [INT_START + DATATYPE_KIND_SIZE, INT_START + (DATATYPE_KIND_SIZE * 2) - 1]
    constant_int_counter = constant_int_range[0] 
    local_int_range = [INT_START + (DATATYPE_KIND_SIZE * 2), INT_START + (DATATYPE_KIND_SIZE * 3) - 1]
    local_int_counter = local_int_range[0]
    temp_int_range = [INT_START + (DATATYPE_KIND_SIZE * 3), INT_START + (DATATYPE_KIND_SIZE * 4) - 1]
    temp_int_counter = temp_int_range[0]


    # Float ranges
    global_float_range = [FLOAT_START, FLOAT_START + DATATYPE_KIND_SIZE - 1]
    global_float_counter = global_float_range[0]
    constant_float_range = [FLOAT_START + DATATYPE_KIND_SIZE, FLOAT_START + (DATATYPE_KIND_SIZE * 2) - 1]
    constant_float_counter = constant_float_range[0]
    local_float_range = [FLOAT_START + (DATATYPE_KIND_SIZE * 2), FLOAT_START + (DATATYPE_KIND_SIZE * 3) - 1]
    local_float_counter = local_float_range[0]
    temp_float_range = [FLOAT_START + (DATATYPE_KIND_SIZE * 3), FLOAT_START + (DATATYPE_KIND_SIZE * 4) - 1]
    temp_float_counter = temp_float_range[0] 

    # Global chars range from 8000 to 11999
    global_char_range = [CHAR_START, CHAR_START + DATATYPE_KIND_SIZE - 1]
    global_char_counter = global_char_range[0] 
    constant_char_range = [CHAR_START + DATATYPE_KIND_SIZE, CHAR_START + (DATATYPE_KIND_SIZE * 2) - 1]
    constant_char_counter = constant_char_range[0] 
    local_char_range = [CHAR_START + (DATATYPE_KIND_SIZE * 2), CHAR_START + (DATATYPE_KIND_SIZE * 3) - 1]
    local_char_counter = local_char_range[0] 
    temp_char_range = [CHAR_START + (DATATYPE_KIND_SIZE * 3), CHAR_START + (DATATYPE_KIND_SIZE * 4) - 1]
    temp_char_counter = temp_char_range[0]

    global_bool_range = [BOOL_START, BOOL_START + DATATYPE_KIND_SIZE - 1]
    global_bool_counter = global_bool_range[0] 
    constant_bool_range = [BOOL_START + DATATYPE_KIND_SIZE, BOOL_START + DATATYPE_KIND_SIZE + 2] # SPECIAL CASE: Boolean constants are only two: true or false. We use the same constants every time
    constant_bool_counter = constant_bool_range[0] 
    local_bool_range = [BOOL_START + (DATATYPE_KIND_SIZE * 2), BOOL_START + (DATATYPE_KIND_SIZE * 3) - 1]
    local_bool_counter = local_bool_range[0] 
    temp_bool_range = [ BOOL_START + (DATATYPE_KIND_SIZE * 3),  BOOL_START + (DATATYPE_KIND_SIZE * 4) - 1]
    temp_bool_counter = temp_bool_range[0] 

    # String constants
    constant_string_range = [STRING_START, STRING_START + DATATYPE_KIND_SIZE - 1]
    constant_string_counter = constant_string_range[0] 

    # Assign global addresses
    def assign_global_address_int(self):
        if self.global_int_counter == self.global_int_range[1]:
            raise Exception('Too many global integers')
        address = self.global_int_counter
        self.global_int_counter += 1
        return address
    
    def assign_global_address_float(self):
        if self.global_float_counter == self.global_float_range[1]:
            raise Exception('Too many global floats')
        address = self.global_float_counter
        self.global_float_counter += 1
        return address
    
    def assign_global_address_char(self):
        if self.global_char_counter == self.global_char_range[1]:
            raise Exception('Too many global chars')
        address = self.global_char_counter
        self.global_char_counter += 1
        return address
    
    def assign_global_address_bool(self):
        if self.global_bool_counter == self.global_bool_range[1]:
            raise Exception('Too many global bools')
        address = self.global_bool_counter
        self.global_bool_counter += 1
        return address

    # Assign constant addresses
    def assign_constant_address_int(self):
        if self.constant_int_counter == self.constant_int_range[1]:
            raise Exception('Too many constant ints')
        address = self.constant_int_counter
        self.constant_int_counter += 1
        return address
    
    def assign_constant_address_float(self):
        if self.constant_float_counter == self.constant_float_range[1]:
            raise Exception('Too many constant floats')
        address = self.constant_float_counter
        self.constant_float_counter += 1
        return address
    
    def assign_constant_address_char(self):
        if self.constant_char_counter == self.constant_char_range[1]:
            raise Exception('Too many constant chars')
        address = self.constant_char_counter
        self.constant_char_counter += 1
        return address
    
    def assign_constant_address_bool(self):
        if self.constant_bool_counter == self.constant_bool_range[1]:
            raise Exception('Too many constant bools')
        address = self.constant_bool_counter
        self.constant_bool_counter += 1
        return address
    
    def assign_constant_address_string(self):
        if self.constant_string_counter == self.constant_string_range[1]:
            raise Exception('Too many constant strings')
        address = self.constant_string_counter
        self.constant_string_counter += 1
        return address

    # Assign local addresses
    def assign_local_address_int(self):
        if self.local_int_counter == self.local_int_range[1]:
            raise Exception('Too many local ints')
        address = self.local_int_counter
        self.local_int_counter += 1
        return address
    
    def assign_local_address_float(self):
        if self.local_float_counter == self.local_float_range[1]:
            raise Exception('Too many local floats')
        address = self.local_float_counter
        self.local_float_counter += 1
        return address
    
    def assign_local_address_char(self):
        if self.local_char_counter == self.local_char_range[1]:
            raise Exception('Too many local chars')
        address = self.local_char_counter
        self.local_char_counter += 1
        return address
    
    def assign_local_address_bool(self):
        if self.local_bool_counter == self.local_bool_range[1]:
            raise Exception('Too many local bools')
        address = self.local_bool_counter
        self.local_bool_counter += 1
        return address
    
    # Assign temporal addresses
    def assign_temp_address_int(self):
        if self.temp_int_counter == self.temp_int_range[1]:
            raise Exception('Too many temp ints')
        address = self.temp_int_counter
        self.temp_int_counter += 1
        return address
    
    def assign_temp_address_float(self):
        if self.temp_float_counter == self.temp_float_range[1]:
            raise Exception('Too many temp floats')
        address = self.temp_float_counter
        self.temp_float_counter += 1
        return address
    
    def assign_temp_address_char(self):
        if self.temp_char_counter == self.temp_char_range[1]:
            raise Exception('Too many temp chars')
        address = self.temp_char_counter
        self.temp_char_counter += 1
        return address
    
    def assign_temp_address_bool(self):
        if self.temp_bool_counter == self.temp_bool_range[1]:
            raise Exception('Too many temp bools')
        address = self.temp_bool_counter
        self.temp_bool_counter += 1
        return address

    def reset_scope_counters(self) -> None:
        self.local_int_counter = self.local_int_range[0]
        self.local_float_counter = self.local_float_range[0]
        self.local_char_counter = self.local_char_range[0]
        self.local_bool_counter = self.local_bool_range[0]
        self.temp_int_counter = self.temp_int_range[0]
        self.temp_float_counter = self.temp_float_range[0]
        self.temp_char_counter = self.temp_char_range[0]
        self.temp_bool_counter = self.temp_bool_range[0]
    
    def assign_mem_address(self, type: str, is_temp: bool = False, is_const: bool = False) -> int:
        if type == types['int']:
            if is_const:
                return self.assign_constant_address_int()
            elif is_temp:
                return self.assign_temp_address_int()
            else:
                return self.assign_local_address_int()
        elif type == types['float']:
            if is_const:
                return self.assign_constant_address_float()
            elif is_temp:
                return self.assign_temp_address_float()
            else:
                return self.assign_local_address_float()
        elif type == types['char']:
            if is_const:
                return self.assign_constant_address_char()
            elif is_temp:
                return self.assign_temp_address_char()
            else:
                return self.assign_local_address_char()
        elif type == types['bool']:
            if is_const:
                return self.assign_constant_address_bool()
            elif is_temp:
                return self.assign_temp_address_bool()
            else:
                return self.assign_local_address_bool()
        else:
            raise Exception(f'Unrecognized type on memory assignment. Got a {type}')        

virtual_memory = VirtualMemory()
    
