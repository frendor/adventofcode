#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:30:25 2020

@author: frendor
"""

DAY = 3
DEBUG = False

PUZZLE_FILE = f"t{DAY}puzzle.input"
EXAMPLE_FILE = f"t{DAY}puzzle.example"


def load_input(filename = PUZZLE_FILE ):
    with open(filename,"r") as file:
        input_lines = file.readlines()
    return input_lines

def walk_through_tag3_part1(filename = PUZZLE_FILE, debug=False):
    pattern = [line.strip() for line in load_input(filename)]
    if debug:
        for line in pattern[:5]:
            print(line)
        print("".center(20,"-"))
    line_length = len(pattern[0])    
    tree_counter = 0 
    for nr,line in enumerate(pattern[1:]):
        if line[(3 + nr*3)%line_length] == "#":
            if debug:
                if nr < 6: 
                    mark_pos = list(line)
                    mark_pos[(3 + nr*3)%line_length] = "X"
                    print("".join(mark_pos))
            tree_counter += 1
        elif debug and nr < 6:
                mark_pos = list(line)
                mark_pos[(3 + nr*3)%line_length] = "O"
                print("".join(mark_pos))
    print(f"Part1 Solution: {tree_counter} Trees ")

def slope_step(step_right,pattern,debug=False):
    tree_counter= 0
    line_length = len(pattern[0])
    for nr,line in enumerate(pattern[1:]):
        if line[(step_right + nr*step_right)%line_length] == "#":
#            if debug:
#                mark_pos = list(line)
#                mark_pos[(step_right + nr*step_right)%line_length] = "X"
#                print("".join(mark_pos))
            tree_counter += 1
#        elif debug:
#                mark_pos = list(line)
#                mark_pos[(step_right + nr*step_right)%line_length] = "O"
#                print("".join(mark_pos))
    #if debug:
    print(f"Right:{step_right} Down: 1 Trees: {tree_counter}")
    return tree_counter

def walk_through_tag3_part2(filename = PUZZLE_FILE, debug=False):
    pattern = [line.strip() for line in load_input(filename)]
#    if debug:
#        for line in pattern:
#            print(line)
#        print("".center(20,"-"))
    tree_counter = 1 
    slopes = [1,3,5,7]
    for col_step in slopes:
        trees = slope_step(col_step, pattern, debug=debug)
        tree_counter *= trees
    
    #nun Right:1 Down:2
    pattern2 = [line for nr,line in enumerate(pattern) if nr%2==0]
    trees2 = slope_step(1, pattern2, debug=debug)
    tree_counter *= trees2
    print(f"Part2 Solution: {tree_counter}")
    
if __name__=="__main__":
    print(" Part 1 ".center(30,"-"))
    walk_through_tag3_part1(debug=True)
    print(" Part 2 ".center(30,"-"))
    walk_through_tag3_part2()