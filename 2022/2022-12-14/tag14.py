#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:33:31 2022

@author: frendor
"""


with open("puzzle","r") as infile:
    data = [[ tuple(map(int,pair.split(","))) for pair in line.strip().split(" -> ")] for line in infile.readlines()]
    

draw_line = lambda p1,p2: [ (dx,dy)  for dx in  range(min(p1[0],p2[0]), max(p1[0],p2[0])+1) for dy in range(min(p1[1],p2[1]), max(p1[1],p2[1])+1) if p1[1] == p2[1] or p1[0] == p2[0] ]

rocks = [draw_line(p1,p2) for block in data for p1,p2 in zip(block,block[1:])]
rock_set = set([complex(*point) for line in rocks for point in line ])       
y_max = max([int(r.imag) for r in rock_set])


def show_cavern(rock_set, full_set,part2=False):    
    x_min = min([int(r.real) for r in full_set])
    x_max = max([int(r.real) for r in full_set])
    y_max = max([int(r.imag) for r in full_set])            
    y_min = 0        
    
    output = "".ljust(5)+"╔"+"".center(x_max-x_min+3,"═")+"╗"
    output += "\n"
    for row in range(y_min, y_max+2):
        if part2 and row == y_max+1:
            output += f"{row:4.0f} ║"+"".center(x_max-x_min+3,"█") + "║"
            output += "\n"
        else:
            output += f"{row:4.0f} ║"+"".join(['█' if complex(col,row) in rock_set else\
                                           '⁖' if complex(col,row) in full_set else\
                                           ' ' for col in range(x_min-1,x_max+2)])+"║"
            output += "\n"
    output += "".ljust(5)+"╚"+"".center(x_max-x_min+3,"═")+"╝"
    output += "\n"
    return output


def produce_sand(full_set, part2):    
    sand_coords = 500
    if sand_coords in full_set:
        return False
    sand_last_coords = 0
    while sand_coords != sand_last_coords:        
        sand_last_coords = sand_coords
        for step in (1j, -1+1j, 1+1j):
            if sand_coords + step not in full_set:
                sand_coords += step
                break
        if not part2 and sand_coords.imag > y_max:
            break
        elif part2 and sand_coords.imag == y_max+1:            
            break
    if part2 or not part2 and not sand_coords.imag > y_max:
        return sand_coords
    else:
        return False


def fill_cavern(part2,save_output=False):
    sand_set = set()
    sand_flow = True
    
    full_set = sand_set.union(rock_set)
    
    while sand_flow:
        sand_coords = produce_sand(full_set, part2=part2)
        if sand_coords:
            full_set.add(sand_coords)
        else:
            sand_flow = False
    part_str = 'Part2' if part2 else 'Part1'
    
    if save_output:
        with open(f"Tag14_{part_str}.out","w") as outfile:
            outfile.write(show_cavern(rock_set, full_set,part2))
    else:
        print(show_cavern(rock_set, full_set,part2))
    print(part_str,len(full_set.difference(rock_set) ))
    

fill_cavern(part2 = False)
fill_cavern(part2 = True, save_output = True)