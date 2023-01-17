#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:19:32 2023

@author: frendor
"""

with open("puzzle","r") as infile:
    data = [tuple(map(int,row.strip().split(","))) for row in infile.readlines()]

get_sides = lambda x,y,z: set([ (a,b,c) for a in [x-0.5, x, x+0.5] 
                                        for b in [y-0.5, y, y+0.5]
                                        for c in [z-0.5, z, z+0.5] 
                                        if (a-x)**2 + (b-y)**2 + (c-z)**2 == 0.5**2])

def get_all_sides(*scan):
    total_set = set()
    for cube_sides in [get_sides(*cube) for cube in scan]:
        total_set.symmetric_difference_update(cube_sides)
    return total_set
    
        
print(f"Part1 - total sides: {len(get_all_sides(*data))}") 

get_min_max = lambda li: [min(li), max(li)]


def water_flow(*scan):

    all_sides = get_all_sides(*scan)
    water_touched_sides = set()
    
    x_list, y_list, z_list = zip(*scan)
    xmin, xmax = get_min_max(x_list)
    ymin, ymax = get_min_max(y_list)
    zmin, zmax = get_min_max(z_list)
    water_filled_blocks = set()

    
    next_blocks = set( [(xmin-1,ymin-1,zmin-1)] )    
    
    
    while len(next_blocks) > 0:
        a_x,a_y,a_z = active_block = next_blocks.pop()
        
        water_filled_blocks.add(active_block)

        this_sides = get_sides(*active_block)
        water_touched_sides.update(all_sides.intersection(this_sides))
        all_sides.difference_update(this_sides)
        
        neighbors = [ (a_x+dx, a_y+dy, a_z+dz) for dx in [-1,0,+1] for dy in [-1,0,1] for dz in [-1,0,1]
                                                if dx**2 + dy**2 + dz**2 == 1
                                                and xmin-1 <= a_x+dx  <= xmax+1
                                                and ymin-1 <= a_y+dy  <= ymax+1 
                                                and zmin-1 <= a_z+dz  <= zmax+1 
                                                and (a_x+dx, a_y+dy, a_z+dz) not in water_filled_blocks
                                                and (a_x+dx, a_y+dy, a_z+dz) not in scan    
                                                ]
        for block in neighbors:
                next_blocks.add(block)
    
    return water_touched_sides
    
print(f"Part2 - water exposed sides: {len(water_flow(*data))}")    
