from numpy import number
from vars_table import VarsTable
from semantic_cube import types

class FuncDirEntry():
    params_list : list
    num_vars_int : number
    num_vars_float : number
    num_vars_char : number
    num_vars_bool : number
    num_temps_int : number
    num_temps_float : number
    num_temps_char : number
    num_temps_bool : number
    starts_at : number
    vars_table : VarsTable
    type : str
    def __init__(self, type: str) -> None:
        self.vars_table = VarsTable()
        self.type = type

    def __str__(self) -> str:
        return f'''type: {self.type} starts_at: {self.starts_at}\n 
        num_vars_int: {self.num_vars_char} num_vars_float: {self.num_vars_float} num_vars_char: {self.num_vars_char} num_vars_bool: {self.num_vars_bool}\n 
        num_temps_int: {self.num_temps_char} num_temps_float: {self.num_temps_float} num_temps_char: {self.num_temps_char} num_temps_bool: {self.num_temps_bool}\n
        vars_table: {self.vars_table}'''
    def __repr__(self) -> str:
        return f'''type: {self.type} starts_at: {self.starts_at}\n 
        num_vars_int: {self.num_vars_char} num_vars_float: {self.num_vars_float} num_vars_char: {self.num_vars_char} num_vars_bool: {self.num_vars_bool}\n 
        num_temps_int: {self.num_temps_char} num_temps_float: {self.num_temps_float} num_temps_char: {self.num_temps_char} num_temps_bool: {self.num_temps_bool}\n
        vars_table: {self.vars_table}'''

class FuncDir():
    func_dir : dict[str, FuncDirEntry] = {}

    def __init__(self) -> None:
        self.create_scope('global')
        self.create_scope('main')

    def __str__(self) -> str:
        return str(self.func_dir)

    def get_func_dir(self) -> dict[str, FuncDirEntry]:
        return self.func_dir

    def create_scope(self, scopeID: str, type: str) -> None:
        self.func_dir[scopeID] = FuncDirEntry(type=type)

    def get_scope_var_table(self, scopeID: str) -> VarsTable:
        return self.func_dir[scopeID].vars_table

    def set_scope_num_params(self, scopeID: str, num_params: number) -> None:
        self.func_dir[scopeID].num_params = num_params

    def set_scope_num_vars(self, scopeID: str, num_vars: number, type: str) -> None:
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

    def set_scope_num_temps(self, scopeID: str, num_temps: number) -> None:
        self.func_dir[scopeID].num_temps = num_temps

    def set_scope_start(self, scopeID, start: number) -> None:
        self.func_dir[scopeID].starts_at = start

