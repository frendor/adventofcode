#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 2020 

@author: frendor
"""

DAY = 5
DEBUG = False

PUZZLE_FILE = f"t{DAY}puzzle.input"
EXAMPLE_FILE = f"t{DAY}puzzle.example"

def load_input(filename = PUZZLE_FILE ):
    with open(filename,"r") as file:
        input_lines = file.readlines()
        
    return [get_placenumber(line.strip()) for line in input_lines]

def get_placenumber(seatplace,debug=DEBUG):
    row = int(seatplace[:7].replace("F","0").replace("B","1"),2)
    place = int(seatplace[-3:].replace("R","1").replace("L","0"),2)
    return (row,place)

'''
Every seat also has a unique seat ID: multiply the row by 8, 
then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
'''
sid = lambda r,p: r*8 + p

def hightest_seatid_part1(boarding_passes):
    max_seatid = 0
    for bpass in boarding_passes:
        max_seatid = max(max_seatid,sid(*bpass))
    print("Part 1: Höchste Seatid: ",max_seatid)

def find_free_seat(boarding_passes,debug=DEBUG):
    '''
    It's a completely full flight, so your seat should be the only missing 
    boarding pass in your list. However, there's a catch: some of the seats 
    at the very front and back of the plane don't exist on this aircraft, 
    so they'll be missing from your list as well.

    Your seat wasn't at the very front or back, though; the seats with 
    IDs +1 and -1 from yours will be in your list.
    '''

    all_seat_ids = [elem for elem in range(8*128)]

    for row,col in boarding_passes:
        all_seat_ids.remove(sid(row,col))
    
    for seat in all_seat_ids:
        if  ((seat-1) not in all_seat_ids)\
        and ((seat+1) not in all_seat_ids):
            print("Part2: Das wird mein Platz sein:",seat)
    #Going through by columns and rows: Problem with aisles/windowseats 
    #all_seats = dict([(row,[sid(row,col) for col in range(8)]) for row in range(128)])            
    #    for row,cols in all_seats.items():
    #        if debug:
    #            print(row,cols)
    #        if any(cols) and not all(cols):
    #            new_col = [sid if 1 <= nr <= 6 and not cols[nr-1] and (not cols[nr+1]) else False for nr,sid in enumerate(cols)]
    #            if any(new_col):
    #               new_col = list(set(new_col))
    #               new_col.remove(False)
    #               print("Part 2: Der letzte freie Platz: ",new_col[0])

if __name__=="__main__":
    boarding_passes = load_input()
    hightest_seatid_part1(boarding_passes)
    find_free_seat(boarding_passes)