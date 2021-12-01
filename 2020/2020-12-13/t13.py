#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:38:05 2020

@author: frendor
"""

from math import ceil
import numpy as np

DAY = 13

VERBOSE = True

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
EXAMPLE2 = f"t{DAY}puzzle.example2"

def load_input(filename = EXAMPLE ):
    with open(filename,"r") as file:
        dep_time, bus_list = [line.strip() for line in file.readlines()]
    return int(dep_time), bus_list

def part1_find_earliest_bus(dep_time, bus_list):
    bus_list =  [int(bus) for bus in bus_list.replace(",x","").split(",")]    
    bus_dict = { (busid*(ceil(dep_time/float(busid)))%dep_time): busid for busid in bus_list }
    next_bus = min(bus_dict.keys())
    return bus_dict[next_bus], next_bus    

def find_timestamp2(bus_list,good_solution=False,verbose=VERBOSE):
    if "x" in bus_list:
        bus_list =  [int(bus) for bus in bus_list.replace("x","0").split(",")]    
        check_list = [ (value,offset) for offset, value in enumerate(bus_list) if value ]
    
    runner,r_offset = check_list[0]
    nn = lambda fac, run, val, off: (fac*run + off)/float(val)

    if good_solution:
        factor=good_solution/runner
    else: 
        factor = 1

    if verbose:  
        #Testing solutions found earlier
        for factor in [17,1370,95055,3018027,15440658,301161171,factor]:
            print(f"Faktortester: {factor}",[nn(factor,runner,val, off) if nn(factor,runner,val, off)%1 else True for val,off in check_list] )

    for r in range(1,len(check_list)):    
        '''This can take a while, brute force-appoarch. But if there is a good_solution, it's a nice test.
           A chained List as approach'''
        if verbose:
            print(f"{r}. Run: {runner}, n0 = {factor}, t0 = {runner*factor}, list = {check_list[:r]}")    

        while not all([ (runner*factor + (offset%value) - r_offset) % value == 0 for value, offset in check_list[:r]]):
            factor += 1
            print(factor)
        if verbose:
            print(f"{r}. Run: Statementlist: ",[ ((value - runner*factor%value)%value, offset%value) for value, offset in check_list])
    return factor*runner    

def tool_solution(bus_list):    

    from sympy.ntheory.modular import solve_congruence

    bus_list =  [int(bus) for bus in bus_list.replace("x","0").split(",")]
    check_list = [(-offset,value) for offset, value in enumerate(bus_list) if value ]
    
    solution = solve_congruence(*check_list)
    return solution[0]

if __name__ == "__main__":
    dep_time,bus_list = load_input(PUZZLE)
    print(f"Departuretime: {dep_time}, Busses: {bus_list}")
    busid, wait_time = part1_find_earliest_bus(dep_time, bus_list)
    print(f"Part1: Next bus: {busid} Leaving in {wait_time} min. Solution {busid*wait_time} busidmin")
    
    good_solution = tool_solution(bus_list)
    
    timestamp = find_timestamp2(bus_list,good_solution)
    
    print(f"Part2: {timestamp}")
    
    #part2_find_bus(bus_list)