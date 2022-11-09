from semantic_cube import types

class VirtualMemory():
    # Global ranges
    # Global ints range from 0 to 3999
    global_int_range = [0, 3999]
    global_int_counter = global_int_range[0] 
    # Global floats range from 4000 to 7999
    global_float_range = [4000, 7999]
    global_float_counter = global_float_range[0]
    # Global chars range from 8000 to 11999
    global_char_range = [8000, 11999]
    global_char_counter = global_char_range[0] 
    # Global bools range from 12000 to 15999
    global_bool_range = [12000, 15999]
    global_bool_counter = global_bool_range[0] 

    # Constant ranges
    # Constant ints range from 16000 to 19999
    constant_int_range = [16000, 19999]
    constant_int_counter = constant_int_range[0] 
    # Constant floats range from 20000 to 23999
    constant_float_range = [20000, 23999]
    constant_float_counter = constant_float_range[0]
    # Constant chars range from 24000 to 27999
    constant_char_range = [24000, 27999]
    constant_char_counter = constant_char_range[0] 
    # Constant bools range from 28000 to 31999
    constant_bool_range = [28000, 31999]
    constant_bool_counter = constant_bool_range[0] 
    # String constants range from 60000 to 63999
    constant_string_range = [60000, 63999]
    constant_string_counter = constant_string_range[0] 

    # local ranges
    # local ints range from 32000 to 35999
    local_int_range = [32000, 35999]
    local_int_counter = local_int_range[0]
    # temp ints range from 36000 to 39999
    temp_int_range = [36000, 39999]
    temp_int_counter = temp_int_range[0]
    # local floats range from 40000 to 43999
    local_float_range = [40000, 43999]
    local_float_counter = local_float_range[0]
    # temp floats range from 44000 to 47999
    temp_float_range = [44000, 47999]
    temp_float_counter = temp_float_range[0] 
    # local chars range from 48000 to 49999
    local_char_range = [48000, 49999]
    local_char_counter = local_char_range[0] 
    # temp chars range from 50000 to 50999
    temp_char_range = [50000, 50999]
    temp_char_counter = temp_char_range[0] 
    # local bools range from 52000 to 53999
    local_bool_range = [52000, 53999]
    local_bool_counter = local_bool_range[0] 
    # temp bools range from 54000 to 55999
    temp_bool_range = [54000, 55999]
    temp_bool_counter = temp_bool_range[0] 

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
    
