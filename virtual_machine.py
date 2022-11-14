from collections import deque
from func_dir import FuncDir
from runtime_memory import RuntimeMemory
from quadruple import Quadruple
from semantic_rules import semantics, CompilationResults
from parser import ali_parser

from vars_table import ConstVarsTable

def generate_constant_memory_segment(consts_table: ConstVarsTable) -> RuntimeMemory:
    mem_segment = RuntimeMemory(
        consts_table.types_counter['int'], 
        consts_table.types_counter['float'], 
        consts_table.types_counter['char'],
        consts_table.types_counter['bool'],
        consts_table.types_counter['string']
    )
    print(f'Empty constant memory segment {mem_segment}')
    for value, const_entry in consts_table.const_vars_table.items():
        mem_segment.assign_content(const_entry.address, value)
    return mem_segment

def virtual_machine(compilation_results: CompilationResults) -> None:
    print(compilation_results.func_dir)
    print(compilation_results.consts_table)
    print(compilation_results.quadruples)
    mem_stack = deque()
    global_scope = compilation_results.func_dir.get_scope('global')
    global_memory = RuntimeMemory(
        global_scope.num_vars_int,
        global_scope.num_vars_float,
        global_scope.num_vars_char,
        global_scope.num_vars_bool
    )
    constants_memory_segment = generate_constant_memory_segment(compilation_results.consts_table)
    print(global_memory)
    print(constants_memory_segment)

if __name__ == '__main__':
    print('Enter file name to be tested (with .al extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    ali_parser.parse(input_str)
    compilation_results : CompilationResults = semantics.get_compilation_results()
    virtual_machine(compilation_results)

