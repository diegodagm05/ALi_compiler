from collections import deque
from parser import ali_parser

import pygame

from func_dir import FuncDirEntry
from quadruple import Quadruple, quadruple_operations
from runtime_memory import RuntimeMemory
from semantic_rules import CompilationResults, semantics


screen = None

def calculate_function_resources(scope: FuncDirEntry) -> list:
    resources = [
        [scope.num_vars_int, scope.num_vars_float, scope.num_vars_char, scope.num_vars_bool],
        [scope.num_temps_int, scope.num_temps_float, scope.num_temps_char, scope.num_temps_bool],
        scope.num_pointer_temps
    ]
    for param in scope.params_list:
        if param == 'i':
            resources[0][0] += 1
        elif param == 'f':
            resources[0][1] += 1
        elif param == 'c':
            resources[0][2] += 1
        elif param == 'b':
            resources[0][3] += 1
    return resources

def convert_string_to_rgb_tuple(color: str) -> tuple[int]:
    if len(color) != 7:
        raise Exception(f'RGB string with 6 digits expected for color parameter. Insted given \'{color}\'')
    color_s = color.lstrip('#')
    return tuple(int(color_s[i:i+2], 16) for i in (0, 2, 4))


def virtual_machine(compilation_results: CompilationResults) -> None:
    # print(compilation_results.func_dir)
    # print(compilation_results.consts_table)
    runtime_memory = RuntimeMemory(compilation_results.consts_table, compilation_results.func_dir)
    quadruples : list[Quadruple] = compilation_results.quadruples
    ip = 0
    call_stack = deque()
    # for i, quad in enumerate(quadruples):
    #     print(f'{i}. {quad}')
    print('--ALi CONSOLE OUTPUT--')
    while True:
        current_quad = quadruples[ip]
        # print("-----------------------------------------")
        # print(f"Quad # {ip} \n Processing {current_quad}  ")
        # print(f'current memory -> \n{runtime_memory.current_mem_segment}')
        # print(f'const memory segment -> \n{runtime_memory.constant_memory_segment}')
        # print(f'global mem segment -> \n{runtime_memory.global_memory_segment}')
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
            result = (left_operand == right_operand)
            runtime_memory.assign_content(current_quad.result, result)
            ip += 1
        elif current_quad.op_code == quadruple_operations['!=']:
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
            print(print_content, end='')
            ip += 1
        elif current_quad.op_code == quadruple_operations['endprint']:
            print()
            ip += 1
        # TODO: Our 'read' operation will in reality involve handling game events
        elif current_quad.op_code == quadruple_operations['read']:
            pass
        elif current_quad.op_code == quadruple_operations['goto']:
            ip = current_quad.result
        elif current_quad.op_code == quadruple_operations['gotot']:
            true_test = runtime_memory.retrieve_content(current_quad.operator1)
            if true_test:
                ip = current_quad.result
            else:
                ip += 1
        elif current_quad.op_code == quadruple_operations['gotof']:
            false_test = runtime_memory.retrieve_content(current_quad.operator1)
            if false_test == False:
                ip = current_quad.result
            else:
                ip += 1
        elif current_quad.op_code == quadruple_operations['gosub']:
            call_stack.append(ip+1)
            runtime_memory.sleep_current_memory()
            ip = current_quad.result
        elif current_quad.op_code == quadruple_operations['era']:
            scope = compilation_results.func_dir.get_scope(current_quad.result)
            resources = calculate_function_resources(scope)
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
        elif current_quad.op_code == quadruple_operations['verify']:
            index_to_verify = runtime_memory.retrieve_content(current_quad.operator1)
            lower_bound = current_quad.operator2
            upper_bound = current_quad.result
            if index_to_verify >= lower_bound and index_to_verify < upper_bound:
                ip += 1
            else:
                raise Exception(f'Index \'{index_to_verify}\' out of bounds. Expected index to be in range \'{lower_bound} - {upper_bound}\'')
        elif current_quad.op_code == quadruple_operations['add_base_address']:
            base_address = current_quad.operator1
            add_value = runtime_memory.retrieve_content(current_quad.operator2)
            result = base_address + add_value
            runtime_memory.current_mem_segment.assign_content(current_quad.result, result, storing_vaddress=True)
            ip += 1
        elif current_quad.op_code == quadruple_operations['multiply_displacement']:
            index_expression = runtime_memory.retrieve_content(current_quad.operator1)
            mutiplier = current_quad.operator2
            result = index_expression * mutiplier
            runtime_memory.current_mem_segment.assign_content(current_quad.result, result)
            ip += 1 
        # Special functions
        elif current_quad.op_code == quadruple_operations['start']:
            pygame.init()
        elif current_quad.op_code == quadruple_operations['update']:
            pygame.display.flip()
        elif current_quad.op_code == quadruple_operations['gen_default_canvas']:
            global screen
            screen = pygame.display.set_mode((current_quad.operator1, current_quad.operator2))
            screen.fill(current_quad.result) # current quad result should be a tuple that represents the rgb value
        elif current_quad.op_code == quadruple_operations['gen_canvas']:
            global screen
            width = runtime_memory.retrieve_content(current_quad.operator1)
            height = runtime_memory.retrieve_content(current_quad.operator2)
            color = runtime_memory.retrieve_content(current_quad.result)
            screen = pygame.display.set_mode((width, height))
            rgb_color = convert_string_to_rgb_tuple(color)
            screen.fill(rgb_color) # current quad result should be a tuple that represents the rgb value
        elif current_quad.op_code == quadruple_operations['set_canvas_tile']:
            caption = runtime_memory.retrieve_content(current_quad.result)
            pygame.display.set_caption(caption)
        elif current_quad.op_code == quadruple_operations['set_canvas_background']:
            global screen
            color = runtime_memory.retrieve_content(current_quad.result)
            rgb_color = convert_string_to_rgb_tuple(color)
            screen.fill(rgb_color) # current quad result should be a tuple that represents the rgb value
        elif current_quad.op_code == quadruple_operations['get_window_width']:
            window_width = screen.get_width()
            runtime_memory.assign_content(current_quad.result, window_width)
        elif current_quad.op_code == quadruple_operations['get_window_height']:
            window_height = screen.get_height(current_quad.result, window_height)
        elif current_quad.op_code == quadruple_operations['get_game_event']:
            for event in pygame.event.get():
                # This is to enable a user to quit a game with CTRL + C in case they are unable to reach quitGame() function in their code
                if event.type == pygame.QUIT:
                    print('Game has been ended by the user.')
                    break
                if event.type == pygame.K_SPACE:
                    key = 0
                elif event.type == pygame.K_LEFT:
                    key = 1
                elif event.type == pygame.K_UP:
                    key = 2
                elif event.type == pygame.K_RIGHT:
                    key = 3
                elif event.type == pygame.K_DOWN:
                    key = 4
                elif event.type == pygame.K_ESCAPE:
                    key = 5
                elif event.type == pygame.KEYUP:
                    key = 6
                elif event.type == pygame.KEYDOWN:
                    key = 7
            runtime_memory.assign_content(current_quad.result, key)
        elif current_quad.op_code == quadruple_operations['draw_game_object']:
            (xpos_vaddr, ypos_vaddr) = current_quad.operator1
            (xsize_vaddr, ysize_vaddr) = current_quad.operator2
            color = runtime_memory.retrieve_content(current_quad.result)
            rgb_color = convert_string_to_rgb_tuple(color)
            xpos = runtime_memory.retrieve_content(xpos_vaddr)
            ypos = runtime_memory.retrieve_content(ypos_vaddr)
            screen_width = screen.get_width()
            screen_height = screen.get_height()
            if xpos < screen_width or xpos > screen_width:
                raise RuntimeError(f'Attempting to draw a game object outside of the screen. Exceeding the width of the game screen. \n Drawing at {xpos} for screen with {screen_width}')
            if ypos < screen_height or ypos > screen_height:
                raise RuntimeError(f'Attempting to draw a game object outside of the screen. Exceeding the height of the game screen. \n Drawing at {ypos} for screen height {screen_height}')
            xsize = runtime_memory.retrieve_content(xsize_vaddr)
            ysize = runtime_memory.retrieve_content(ysize_vaddr)
            gameObject = pygame.Surface((xsize, ysize))
            gameObject.fill(rgb_color) # current quad result should be a tuple that represents the rgb value
            screen.blit(gameObject, (xpos, ypos))
        else:
            raise RuntimeError('Unknown action for virtual machine')
    print('\n--END OF ALi CONSOLE OUTPUT--')
    

if __name__ == '__main__':
    print('Enter file name to be tested (with .al extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    ali_parser.parse(input_str)
    compilation_results : CompilationResults = semantics.get_compilation_results()
    virtual_machine(compilation_results)

