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
        oper_list_raw = [line.strip().split() for line in file.readlines()]
        oper_list = [[elem,int(arg)] for elem,arg in oper_list_raw]
    return oper_list 

def oper_list_runner(oper_list, 
                     accumulator = 0, 
                     step_list = [], 
                     line_nr = 0,  
                     debug=DEBUG):
    
    while (line_nr not in step_list) and (0 <= line_nr <=len(oper_list)-1):
        step_list.append(line_nr)
        tmp_com, tmp_arg = oper_list[line_nr]
        accumulator += (tmp_com =="acc")*tmp_arg

        line_nr += {"nop":1,
                     "acc":1,
                     "jmp":tmp_arg}[tmp_com]
        
    if debug:
        print(f"{tmp_com} {tmp_arg}, Accumulator: {accumulator}")
    return line_nr in step_list, 0 <= line_nr <= len(oper_list)+1, accumulator

def oper_list_tester(oper_list, debug=DEBUG):
    
    used_steps = []
    accumulator = 0
    line_nr=0

    while (line_nr not in used_steps) and (0 <= line_nr <=len(oper_list)-1):
        
        tmp_com, tmp_arg = oper_list[line_nr]

        if tmp_com == "acc":
            accumulator += tmp_arg
        else:
            #Liste wird hier dauerhaft veraendert, interessiert nicht mehr, was war. 
            #Besser kein Replace sonder neue Unterliste fuer den Schritt erzeugen lassen.

            #new_oper_list = oper_list.copy()
            #new_oper_list[line_nr][0] = new_oper_list[line_nr][0].replace(tmp_com,{"nop":"jmp","jmp":"nop"}[tmp_com])
            oper_list[line_nr][0] = oper_list[line_nr][0].replace(tmp_com,{"nop":"jmp","jmp":"nop"}[tmp_com])
            
            is_loop, in_bound, accu = oper_list_runner(oper_list, 
                                                       accumulator = accumulator, 
                                                       step_list = used_steps.copy(), 
                                                       line_nr = line_nr,
                                                       debug=debug)
            if not is_loop and in_bound: 
                return is_loop, in_bound, accu

        used_steps.append(line_nr)
        line_nr += {"nop":1,
                    "acc":1,
                    "jmp":tmp_arg}[tmp_com]
        
        if debug:
            print(f"Test: {tmp_com} {tmp_arg}, Accumulator: {accumulator}")
    
    print("Tester: No simple replacement found.")
    return line_nr in used_steps, 0 <= line_nr <=len(oper_list), accumulator
    
    
if __name__ == "__main__":
    oper_list = load_input(PUZZLE)

    #Part 1:
    is_loop, in_boundary, accumulator = oper_list_runner(oper_list,debug=DEBUG)
    print(f"Part1: Loops starts now. (Loop-Detection: {is_loop}) final accumulator: {accumulator}")
    #Part 2: Tester
    is_loop, in_boundary, accumulator = oper_list_tester(oper_list,debug=DEBUG)
    print(f"Part2: Loop-Detection: {is_loop}, Found exit: {in_boundary} with final accumulator: {accumulator}")