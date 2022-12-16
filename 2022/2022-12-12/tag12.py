#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:53:00 2022

@author: frendor
"""


from string import ascii_lowercase,ascii_uppercase
from math import inf
from queue import PriorityQueue

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Point:
    steps: int
    coord: Any=field(compare=False)

def print_field(ev_map, visited_points = set()):
    max_row = int(max([k.imag for k in ev_map.keys()]))
    max_col = int(max([k.real for k in ev_map.keys()]))
    for row in range(max_row):
        print("".join([ascii_lowercase[int(elevation_map[complex(col,row)])] \
                                           if complex(col,row) not in visited_points else\
                       "▇"                  
                                           
                                       for col in range(max_col)]))


with open("puzzle","r") as infile:
    data = infile.read()

elevation_map = {complex(col,row):ascii_lowercase.index(val) if val in ascii_lowercase else val 
                                                             for row,line in enumerate(data.split("\n"))
                                                             for col, val in enumerate(line) }

start_point, end_point = [coord for coord,val in elevation_map.items() for target in ("S","E") if val == target]

elevation_map[start_point] = 0
elevation_map[end_point] = 25

def get_path(fd,e_point):
    s_point = [v[1] for k,v in fd.items() if v[0] == 0][0]
    
    last_knot = fd[e_point][1]
    way = set([last_knot])    
    while last_knot != s_point:
        last_knot = fd[last_knot][1]
        way.add(last_knot)
    return way

def pathfinder(starting_point):
    field_dict = {starting_point:(0,starting_point)}
    visited_points = set()
    
    PQ = PriorityQueue()
    PQ.put(Point(0,starting_point))
       
    while not PQ.empty():
        hier = PQ.get()
        fewest_steps, active_coord = hier.steps, hier.coord
        #print(f"{active_coord} | {fewest_steps:3.0f} | {elevation_map[active_coord]} | ")
        if active_coord in visited_points:
            continue
        if active_coord == end_point:
            break
        visited_points.add(active_coord)
        actual_height = elevation_map[active_coord]
        possible_steps = [active_coord+ds for ds in [1,-1,1j,-1j] if active_coord+ds in elevation_map 
                                                                  and elevation_map[active_coord+ds] <= actual_height + 1 
                                                                  and active_coord+ds not in visited_points  ]
        
        for new_coord in possible_steps:
            known_steps, last_knot = field_dict.setdefault(new_coord,(inf,[]))
    
            if fewest_steps + 1 < known_steps:
                field_dict[new_coord] = (fewest_steps + 1, active_coord)
            PQ.put(Point(field_dict[new_coord][0],new_coord))
    
    if end_point in field_dict:
        return field_dict
    else:
        #print("Endpunkt nicht erreichbar von {starting_point}")
        #print_field(elevation_map, visited_points)
        return False

show_fields = True

fd_p1 = pathfinder(start_point)
print(f"Part1: {fd_p1[end_point][0]} Schritte")
if show_fields:
    way_p1 = get_path(fd_p1, end_point)
    print_field(elevation_map,way_p1)

##################### Part2
field_list = [pathfinder(k) for k,v in elevation_map.items() if v == 0]
field_list = [fd for fd in field_list if fd]
fewest_steps,shortest_path_nr = sorted([(fl[end_point][0],nr) for nr,fl in enumerate(field_list)])[0]
print(f"Part2: {fewest_steps} Schritte in pfad {shortest_path_nr}")

if show_fields:
    fd_p2 = field_list[shortest_path_nr]
    
    way_p2 = get_path(fd_p2, end_point)
    print_field(elevation_map, way_p2)