from vars_table import VarsTable

class FuncDir():
    func_dir = {
        'global': VarsTable(),
        'main': VarsTable(),
    }

    def create_scope(self, scopeID: str) -> None:
        self.func_dir[scopeID] = VarsTable()

    def get_scope(self, scopeID: str) -> VarsTable:
        return self.func_dir[scopeID]
