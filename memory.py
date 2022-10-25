from semantic_cube import types

class Memory():
    int_counter = 1000 # Ints will range from 1000 to 3999
    temp_int_counter = 4000 # Temp ints will range from 4000 to 8999
    float_counter = 9000 # Floats will range from 9000 12999
    temp_float_counter = 13000 # Temp floats will range from 13000 to 17999
    char_counter = 18000 # Chars will range from 18000 to 19999
    temp_char_counter = 20000 # Temp chars will range from 20000 to 21999
    bool_counter = 22000 # Bools will range from 22000 to 23999
    temp_bool_counter = 24000 # Temp bools will range from to 25999
    const_counter = 30000 # Constants will range from 30000 to 35000

    memory = {}

    def assign_mem_address(self, type: str, is_temp: bool) -> int:
        if type == types['int']:
            if is_temp:
                if self.temp_int_counter > 8999:
                    raise Exception('Too many temporal integers')
                else:
                    address = self.temp_int_counter
                    self.temp_int_counter += 1
            else:
                if self.int_counter > 3999:
                    raise Exception('Too many integers')
                else:
                    address = self.int_counter
                    self.int_counter += 1
        elif type == types['float']:
            if is_temp:
                if self.temp_float_counter > 17999:
                    raise Exception('Too many temporal floats')
                else:
                    address = self.temp_float_counter
                    self.temp_float_counter += 1
            else:
                if self.float_counter > 12999:
                    raise Exception('Too many floats')
                else:
                    address = self.float_counter
                    self.float_counter += 1
        elif type == types['char']:
            if is_temp:
                if self.temp_char_counter > 21999:
                    raise Exception('Too many temporal chars')
                else:
                    address = self.temp_char_counter
                    self.temp_char_counter += 1
            else:
                if self.char_counter > 19999:
                    raise Exception('Too many chars')
                else:
                    address = self.char_counter
                    self.char_counter += 1
        elif type == types['bool']:
            if is_temp:
                if self.temp_bool_counter > 25999:
                    raise Exception('Too many temporal booleans')
                else:
                    address = self.temp_bool_counter
                    self.temp_bool_counter += 1
            else:
                if self.bool_counter > 23999:
                    raise Exception('Too many booleans')
                else:
                    address = self.bool_counter
                    self.bool_counter += 1
        elif type == 'CONST':
            if self.const_counter > 35000:
                raise Exception("Too many constants")
            else:
                address = self.const_counter
                self.const_counter += 1
        else:
            raise Exception('Unrecognized type on memory assignment')        
        return address

    def get_mem_content(self, address: int):
        return self.memory[address]

    def set_mem_content(self, address: int, content):
        self.memory[address] = content

virtual_memory = Memory()
    
