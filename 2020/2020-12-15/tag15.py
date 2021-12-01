#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DAY = 15

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"

def load_input(filename = EXAMPLE ):
    with open(filename,"r") as file:
        seq_list = [line.strip() for line in file.readlines()]
    return seq_list 

def find_spoken_number(sequence,limit=2020):
    sequence = [int(elem) for elem in sequence.split(",")]
    
    while len(sequence) < limit:
        current_number = sequence.pop()
        
        if current_number in sequence:
            latest_pos = len(sequence) - 1 - list(reversed(sequence)).index(current_number)
            next_number = len(sequence) - latest_pos
            sequence.extend([current_number, next_number])
        else:
            sequence.extend([current_number,0])
    return sequence[-1]

def find_spoken_number_v2(sequence,limit=2020):
    seq_list = [(int(elem),nr+1) for nr,elem in enumerate(sequence.split(","))]

    current_value, step_counter = seq_list.pop()    
    seq_dict = dict(seq_list)
    
    while step_counter < limit:
        if current_value in seq_dict:
            next_value = step_counter - seq_dict[current_value]
        else:
            next_value = 0 
        seq_dict[current_value] = step_counter 
        step_counter += 1
        current_value = next_value
    
    return current_value
            
if __name__=="__main__":
    input_list = load_input(PUZZLE)
    for sequence in input_list:
        the_2020_number = find_spoken_number_v2(sequence, limit=2020)
        print(f"Part1: 2020th spoken number of Sequence {sequence} is {the_2020_number}." )
    the_30mio_number = find_spoken_number_v2(sequence, limit=30_000_000)
    print("Part2: 30000000th spoken number is ", the_30mio_number)