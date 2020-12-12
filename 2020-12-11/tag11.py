#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:31:45 2020

@author: frendor
"""

import numpy as np
import time
DAY = 11

VERBOSE = True

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
EXAMPLE2 = f"t{DAY}puzzle.example2"

def load_input(filename = PUZZLE ):
    with open(filename,"r") as file:
        field_list = np.array([list(line.strip()) for line in file.readlines()],dtype=object)
    return field_list 

def sub_field(field,row,col):
    row_len, col_len = field.shape
    row_low = max(0,row-1)
    row_high = min(row_len, row+2)
    col_high = min(col_len, col+2)
    col_low = max(0,col-1)
    return field[row_low:row_high,col_low:col_high]

def part1_will_state_switch(field,row,col):
    neighbors = sub_field(field,row,col)
    if neighbors.sum().count('#')==0 and field[row][col]!=".":
        return True
    elif (field[row][col]=="#") and neighbors.sum().count("#") >= 5:
        return True
    return False

in_field = lambda field,row,col: 0<=row<field.shape[0] and 0<=col<field.shape[1]

def part2_will_state_switch(field,row,col):
    max_len = np.max([field.shape[0]-row, field.shape[1]-col,row,col])
    theta_set = [ np.array([nrow,ncol]) for nrow in [-1,0,1] for ncol in [-1,0,1] if not (nrow==ncol and nrow == 0) ] 
    switch_list = []
    for theta in theta_set:
        for r in range(1,max_len):   
            coords = r * theta + [row,col]
            if not in_field(field,*coords) or field[coords[0],coords[1]] == "L":
                switch_list.append(0)
                break
            elif field[coords[0],coords[1]] == "#":
                switch_list.append(1)
                break
    if field[row][col] == "L" and sum(switch_list)==0:
        return True
    elif field[row][col] == "#" and sum(switch_list)>=5:
        return True
    else:
        return False
        
def one_step(field,part=1):
    will_switch_state = {1:part1_will_state_switch,
                         2:part2_will_state_switch}[part]
    
    row_len, col_len = field.shape
    new_field = field.copy()
    for row in range(row_len):
        for col in range(col_len):
            if will_switch_state(field,row,col):
                new_field[row][col] = {"L":"#", "#":"L"}[field[row][col]]
    return new_field

count_not_free_seats = lambda field: field.sum().count("#")

def print_field(field):
    print("\n".join(np.sum(field,axis=1)))

def find_stable_state(field,part,verbose=VERBOSE):
    last_not_free_seats = 1
    run = 0
    while last_not_free_seats != count_not_free_seats(field):
        last_not_free_seats = count_not_free_seats(field)
        if verbose:
            print(" {} ".format(run).center(20,"-"))
            print_field(field)
            print(f"Step {run} - Not free seats: ", count_not_free_seats(field))
        field = one_step(field,part)
        run += 1
    return last_not_free_seats, run

if __name__ == "__main__":
    field = load_input()
    seats, run = find_stable_state(field, part=1, verbose=False)
    print(f"Part1: Field is stable after {run} steps. In the end occupied seats: {seats}")
    seats, run = find_stable_state(field, part=2, verbose=False)
    print(f"Part2: Field is stable after {run} steps. In the end occupied seats: {seats}")
    