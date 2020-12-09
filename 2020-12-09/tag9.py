#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:52:34 2020

@author: frendor
"""

DAY = 9

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
    
def load_input(filename = PUZZLE ):
    with open(filename,"r") as file:
        input_list = [int(line.strip()) for line in file.readlines()]
    return input_list 

valid_number = lambda number,prelist: any([((number-elem) in prelist[nr:]) for nr,elem in enumerate(prelist[:-1]) ])

def part1_find_first_invalid_number(puzzle_list,length_of_preamble):
    for nr,value in enumerate(puzzle_list[length_of_preamble:]):
        if not valid_number(value,puzzle_list[nr:length_of_preamble+nr]):
            return value

def part2_find_set(puzzle_input,first_invalid):
    for nr in range(len(puzzle_input)):
        sub_nr = nr+1  
        while first_invalid > sum(puzzle_input[nr:sub_nr]):
            sub_nr += 1
        if first_invalid == sum(puzzle_input[nr:sub_nr]):
            return puzzle_input[nr:sub_nr]
        
if __name__ == "__main__":
    puzzle_input = load_input(PUZZLE)
    first_invalid = part1_find_first_invalid_number(puzzle_input,25)
    print(f"First invalid number in list is: {first_invalid}")
    con_set = part2_find_set(puzzle_input,first_invalid)
    print("For {0} the contagious set is {1}. Solution is {2}".format(
                    first_invalid,
                    con_set,
                    min(con_set)+max(con_set)))
    