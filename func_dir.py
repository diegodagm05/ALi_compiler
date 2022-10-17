from vars_table import Vars_Table

class Func_Dir():
    func_dir = {
        'global': Vars_Table(),
        'main': Vars_Table(),
    }

    def create_scope(self, scopeID: str) -> None:
        self.func_dir[scopeID] = Vars_Table()

    def get_scope(self, scopeID: str) -> Vars_Table:
        return self.func_dir[scopeID]
