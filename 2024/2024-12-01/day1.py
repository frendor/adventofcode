#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:44:59 2024

@author: frendor
"""

def read_lists(puzzle_file):
    with open(puzzle_file,"r") as infile:
        data = [[int(nr) for nr in line.split()] for line in infile.readlines()]
        
    return data   

def teil1(puzzle_file):
    diff = lambda z1,z2: abs(z2 - z1) 

    data = read_lists(puzzle_file)
    
    input_list = [sorted(l) for l in zip(*data) ]    
    diff_list = [diff(*pair) for pair in zip(*input_list)]
    # print(f"sum({diff_list}): {sum(diff_list)}")
    
    return sum(diff_list)

def teil2(puzzle_file):
    
    data = read_lists(puzzle_file)
    l1,l2 = zip(*data)
    return sum([ elem * l2.count(elem) for elem in l1 ])
    
if __name__ == "__main__":
    for l in ["example","day1_input"]:
        print(f"Teil 1: {l} - T1: ", teil1(l) )
        print(f"Teil 2: {l} - T2: ", teil2(l) )
    
    #print("Teil 1: Puzzle -", teil1("day1_input"))
