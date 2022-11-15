from collections import deque
from func_dir import FuncDir
from runtime_memory import RuntimeMemory
from quadruple import Quadruple, quadruple_operations
from semantic_rules import semantics, CompilationResults
from parser import ali_parser
from vars_table import ConstVarsTable


def virtual_machine(compilation_results: CompilationResults) -> None:
    runtime_memory = RuntimeMemory(compilation_results.consts_table, compilation_results.func_dir)
    quadruples : list[Quadruple] = compilation_results.quadruples
    ip = 0
    call_stack = deque()
    while True:
        current_quad = quadruples[ip]
        if current_quad.op_code == quadruple_operations['endprogram']:
            break 
        elif current_quad.op_code == quadruple_operations['+']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand + right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['-']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand - right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['*']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand * right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['/']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand / right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['&&']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand and right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['||']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand or right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['==']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand == right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['==']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand != right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['>']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand > right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['<']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand < right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['<']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand < right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['>=']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand >= right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['<=']:
            left_operand = runtime_memory.retrieve_content(current_quad.operator1)
            right_operand = runtime_memory.retrieve_content(current_quad.operator2)
            result = left_operand <= right_operand
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['=']:
            result = runtime_memory.retrieve_content(current_quad.operator1)
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['!']:
            result = runtime_memory.retrieve_content(current_quad.operator1)
            result = not result
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['print']:
            print_content = runtime_memory.retrieve_content(current_quad.result)
            print(print_content)
        # TODO: Our 'read' operation will in reality involve handling game events
        elif current_quad.op_code == quadruple_operations['read']:
            pass
        elif current_quad.op_code == quadruple_operations['goto']:
            ip = current_quad.result
        elif current_quad.op_code == quadruple_operations['gotot']:
            true_test = runtime_memory.retrieve_content(current_quad.operator1)
            if true_test:
                ip = current_quad.result
        elif current_quad.op_code == quadruple_operations['gotof']:
            false_test = runtime_memory.retrieve_content(current_quad.operator1)
            if false_test == False:
                ip = current_quad.result
        elif current_quad.op_code == quadruple_operations['gosub']:
            call_stack.append(ip)
            runtime_memory.sleep_current_memory()
            ip = current_quad.result
        elif current_quad.op_code == quadruple_operations['era']:
            resources = current_quad.result
            runtime_memory.create_mem_segment(resources)
            ip += 1
        elif current_quad.op_code == quadruple_operations['parameter']:
            # We need to specifically access the current memory to retrieve the values and copy them to our activation record before it is set as the current memory
            copy_value = runtime_memory.current_mem_segment.retrieve_content(current_quad.operator1)
            runtime_memory.activation_record.assign_content(current_quad.result, copy_value)
            ip += 1
        elif current_quad.op_code == quadruple_operations['endfunc']:
            runtime_memory.destroy_current_mem_segment()
            previous_call = call_stack.pop()
            ip = previous_call
        elif current_quad.op_code == quadruple_operations['return']:
            result = runtime_memory.retrieve_content(current_quad.operator1)
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        else:
            raise RuntimeError('Unknown action for virtual machine')

        




if __name__ == '__main__':
    print('Enter file name to be tested (with .al extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    ali_parser.parse(input_str)
    compilation_results : CompilationResults = semantics.get_compilation_results()
    virtual_machine(compilation_results)

