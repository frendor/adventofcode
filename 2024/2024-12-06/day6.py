#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:18:12 2024

@author: frendor
"""

with open("puzzle") as infile:
    data=infile.read().strip()

new_direction = lambda current_direction: direction_circle[(direction_circle.index(current_direction)+1)%4]

def guard_walk(start_pos, start_direction, blocks, x_limit, y_limit):
    positions = set()
    current_position = start_pos
    direction = start_direction 
    while 0 <= current_position.real <x_limit and 0<=current_position.imag < y_limit:
        positions.add(current_position)
        if current_position + direction in blocks:
            direction = new_direction(direction)
        current_position = current_position + direction
        #print(f"Now: {current_position}, heading to {direction}")
    #print(f"{len(positions)} Felder wurden betreten")
    return positions

def guard_walk2(start_pos, start_direction, blocks, x_limit, y_limit):
    loop_control = set()
    
    current_position = start_pos
    direction = start_direction 
    while (0 <= current_position.real <= x_limit and 0<=current_position.imag <= y_limit):    
        if (current_position, direction) in loop_control:
            return True
        else:
            loop_control.add((current_position, direction))
        
        while current_position + direction in blocks:
            direction = new_direction(direction)
                 
        current_position = current_position + direction
    return False


def show_field(blocks, positions, xlim, ylim,extra_block=set()):
    print("\n".join([ build_line(y,blocks,positions,xlim,extra_block) for y in range(ylim) ]))
        
def build_line(y, blocks, positions, xlim , extra_block = set()):        
    line=[]
    for x in range(xlim):
        if x+1j*y in blocks:
           line.append("#")
        elif x+1j*y in extra_block:
            line.append("O")
        elif x+1j*y in positions:
            line.append("X")
        else:
            line.append(".")
    return "".join(line)

    
if __name__ == "__main__":
    
    x_limit = len(data.split("\n")[0].strip())
    y_limit = len(data.split("\n"))

    print(f"Das Feld ist {x_limit} x {y_limit}")

    blocks = set([pos+1j*line for line, row in enumerate(data.split("\n")) for pos, char in enumerate(row) if char =="#"])
    guard_pos, guard_char = [(pos+1j*line,char) for line, row in enumerate(data.split("\n")) for pos, char in enumerate(row) if char in ["^","<",">","v"]][0]
    guard_dict = {"^":-1j,
                  ">":1,
                  "v":1j,
                  "<":-1}
    guard_base = guard_dict[guard_char]
    direction_circle = [-1j,1,1j,-1]
    print(f"Guard is in {guard_pos}, heading to {guard_base}")


    positions = guard_walk(guard_pos, guard_base, blocks, x_limit, y_limit )

    print(f"Teil1: {len(positions)} Felder wurden betreten.")
    
    loops = 0
    for extra_block in positions:
        if guard_walk2(guard_pos, guard_base, blocks.union({extra_block}), 
                                    x_limit, y_limit):
            loops+=1
    print(f"Teil2: {loops} Loops gefunden.")
    
