#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020-12-08

@author: frendor
"""

DAY = 8
DEBUG = False

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
    
def load_input(filename = PUZZLE ):
    with open(filename,"r") as file:
        oper_list = [line.strip() for line in file.readlines()]
    return oper_list 
    
def oper_list_runner(oper_list, 
                     accumulator = 0, 
                     step_list = [],
                     line_nr = 0):
        
    while (line_nr not in step_list) \
      and (0 <= line_nr <=len(oper_list)-1):
        
        step_list.append(line_nr)
        tmp_com, tmp_arg = oper_list[line_nr].split()
        
        accumulator += (tmp_com == 'acc')*int(tmp_arg)
        line_nr += 1 + (tmp_com == 'jmp')*(int(tmp_arg) - 1)
        
    return line_nr in step_list, 0 <= line_nr <= len(oper_list), accumulator, step_list 

def oper_list_tester(oper_list, orig_step_list, debug=DEBUG):

    accumulator = 0
    loop_list = orig_step_list.copy()
    for line_nr in orig_step_list:
        
        tmp_com, tmp_arg = oper_list[line_nr].split()
        if tmp_com == 'acc':
            accumulator += int(tmp_arg)
        
        next_line_nr = line_nr + 1 + (tmp_com == 'nop')*(int(tmp_arg) - 1)
        
        is_loop, in_bound, accu, loop_list = oper_list_runner(oper_list, 
                                        accumulator = 0, 
                                        step_list = loop_list,
                                        line_nr = next_line_nr 
                                        )
        
        if not is_loop and in_bound: 
            return is_loop, in_bound, accu+accumulator

    print("Tester: No simple replacement found. Quitting")
    return True, False, accumulator
    
    
if __name__ == "__main__":
    oper_list = load_input(PUZZLE)
    #Part 1:
    is_loop, in_boundary, accumulator,step_list = oper_list_runner(oper_list)
    print(f"Part1: Loops starts now. (Loop-Detection: {is_loop}) final accumulator: {accumulator}")
    #Part 2: Tester    
    is_loop, in_boundary, accumulator = oper_list_tester(oper_list,step_list)
    print(f"Part2: Loop-Detection: {is_loop}, Found exit: {in_boundary} with final accumulator: {accumulator}")
