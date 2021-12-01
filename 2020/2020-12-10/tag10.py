#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 2020

@author: frendor
"""

DAY = 10

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
EXAMPLE2 = f"t{DAY}puzzle.example2"
    
def load_input(filename = PUZZLE ):
    with open(filename,"r") as file:
        input_list = [int(line.strip()) for line in file.readlines()]
    return input_list 
  
def part1_adapter_chain(adapter_list):
    adapter_list = sorted(adapter_list+[0]) # +0 for the source
    adapter_diff_list = []
    for nr,adapter in enumerate(adapter_list[1:]):
        adapter_diff_list.append(adapter - adapter_list[nr])
    adapter_diff_list.append(3) #for the build-in
    return adapter_diff_list
    
def part2_adapter_combinations(adapter_diff_list):
    str_list = "".join([str(elem) for elem in adapter_diff_list])
    chain_list = ("".join(str_list)).split('3')
    #The longest +1 chain found is +1+1+1+1+ 
    chain_factor_dict = {0:1, 1:1, 2:2, 3:4, 4:7} # solved with pencil&paper
    chain_factors = [chain_factor_dict[len(chain)] for chain in chain_list]
    rec_multi = lambda numbers,func: numbers[0] * func(numbers[1:],rec_multi) if len(numbers)>1 else numbers[0] 
    return rec_multi(chain_factors,rec_multi) 
          
if __name__ == "__main__":
    puzzle_input = load_input()
    #Part1: Longest Jolt-Chain
    adapter_diff_list = part1_adapter_chain(puzzle_input)
    diff_list = [adapter_diff_list.count(elem+1) for elem in range(3)]
    print("Part1: Differences: 1: {0}, 2: {1}, 3:{2}, Summe: {3}".format(*diff_list,
                                                          diff_list[0]*diff_list[2]))
    #Part2: Possible jolt-combinations
    jolt_combinations = part2_adapter_combinations(adapter_diff_list)
    print("Part2: Possible jolt-combinations: ",jolt_combinations)