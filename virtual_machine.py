from collections import deque
from func_dir import FuncDir
from runtime_memory import RuntimeMemory
from quadruple import Quadruple
from semantic_rules import semantics, CompilationResults
from parser import ali_parser

def process_quads(quadruple: Quadruple, func_dir: FuncDir) -> None:
    mem_stack = deque()
    global_scope = func_dir.get_scope('global')
    global_memory = RuntimeMemory()


if __name__ == '__main__':
    print('Enter file name to be tested (with .al extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    ali_parser.parse(input_str)
    compilation_results : CompilationResults = semantics.get_compilation_results()
    print(compilation_results.func_dir)
    print(compilation_results.consts_table)
    print(compilation_results.quadruples)

