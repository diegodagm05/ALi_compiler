from vars_table import VarsTable
from semantic_cube import types

class FuncDirEntry():
    def __init__(self, type: str) -> None:
        self.vars_table = VarsTable()
        self.type = type
        self.params_list = []
        self.num_vars_int = 0
        self.num_vars_float = 0
        self.num_vars_char = 0
        self.num_vars_bool = 0
        self.num_temps_int = 0
        self.num_temps_float = 0
        self.num_temps_char = 0
        self.num_temps_bool = 0
        self.starts_at = -1
        self.is_returning_value = False

    def __str__(self) -> str:
        return f'''type: {self.type} starts_at: {self.starts_at}\n 
        num_vars_int: {self.num_vars_int} num_vars_float: {self.num_vars_float} num_vars_char: {self.num_vars_char} num_vars_bool: {self.num_vars_bool}\n 
        num_temps_int: {self.num_temps_int} num_temps_float: {self.num_temps_float} num_temps_char: {self.num_temps_char} num_temps_bool: {self.num_temps_bool}\n
        params_list : {self.params_list} \n
        vars_table: {self.check_for_vars_table()}'''
        
    def __repr__(self) -> str:
        return f'''type: {self.type} starts_at: {self.starts_at}\n 
        num_vars_int: {self.num_vars_int} num_vars_float: {self.num_vars_float} num_vars_char: {self.num_vars_char} num_vars_bool: {self.num_vars_bool}\n 
        num_temps_int: {self.num_temps_int} num_temps_float: {self.num_temps_float} num_temps_char: {self.num_temps_char} num_temps_bool: {self.num_temps_bool}\n
        params_list : {self.params_list} \n
        vars_table: {self.check_for_vars_table()} \n'''

    # helper for printing this class
    def check_for_vars_table(self):
        if hasattr(self, 'vars_table'):
            return self.vars_table
        else:
            return ''

    def release_scope_vars_table(self):
        del self.vars_table

class FuncDir():
    def __init__(self) -> None:
        self.func_dir : dict[str, FuncDirEntry] = {}
        self.create_scope('global', 'void')
        self.create_scope('main', 'void')

    def __str__(self) -> str:
        return str(self.func_dir)

    def get_func_dir(self) -> dict[str, FuncDirEntry]:
        return self.func_dir

    def get_scope(self, scopeID: str):
        if scopeID not in self.func_dir:
            raise Exception(f'Uknown scope being referenced {scopeID}')
        else:
            return self.func_dir[scopeID]

    def create_scope(self, scopeID: str, type: str) -> None:
        self.func_dir[scopeID] = FuncDirEntry(type=type)

    def get_scope_var_table(self, scopeID: str) -> VarsTable:
        return self.func_dir[scopeID].vars_table

    def set_scope_num_params(self, scopeID: str, num_params: int) -> None:
        self.func_dir[scopeID].num_params = num_params

    def add_to_param_list(self, scopeID: str, param_type: str) -> None:
        self.func_dir[scopeID].params_list.insert(0, param_type[0])

    def set_scope_num_vars(self, scopeID: str, num_vars: int, type: str) -> None:
        if type == types['int']:
            self.func_dir[scopeID].num_vars_int = num_vars
        elif type == types['float']:
            self.func_dir[scopeID].num_vars_float = num_vars
        elif type == types['char']:
            self.func_dir[scopeID].num_vars_char = num_vars
        elif type == types['bool']:
            self.func_dir[scopeID].num_vars_bool = num_vars
    
    def increment_scope_num_temp_vars(self, scopeID: str, type: str) -> None:
        if type == types['int']:
            self.func_dir[scopeID].num_temps_int += 1
        elif type == types['float']:
            self.func_dir[scopeID].num_temps_float += 1
        elif type == types['char']:
            self.func_dir[scopeID].num_temps_char += 1
        elif type == types['bool']:
            self.func_dir[scopeID].num_temps_bool += 1

    def set_scope_num_temps(self, scopeID: str, num_temps: int) -> None:
        self.func_dir[scopeID].num_temps = num_temps

    def set_scope_start(self, scopeID, start: int) -> None:
        self.func_dir[scopeID].starts_at = start

    def set_is_returning_value(self, scopeID: str, is_returning_val: bool) -> None:
        self.func_dir[scopeID].is_returning_value = is_returning_val