from numpy import number
from vars_table import VarsTable
from semantic_cube import types

class FuncDirEntry():
    params_list : list
    resources : tuple
    starts_at : number
    vars_table : VarsTable
    type : str
    def __init__(self, type: str) -> None:
        self.vars_table = VarsTable()
        self.type = type
class FuncDir():
    func_dir : dict[str, FuncDirEntry] = {}

    def __init__(self) -> None:
        self.create_scope('global')
        self.create_scope('main')

    def get_func_dir(self) -> dict[str, FuncDirEntry]:
        return self.func_dir

    def create_scope(self, scopeID: str, type: str) -> None:
        self.func_dir[scopeID] = FuncDirEntry(type=type)

    def get_scope_var_table(self, scopeID: str) -> VarsTable:
        return self.func_dir[scopeID].vars_table
