#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:36:31 2022

@author: frendor
"""

from operator import itemgetter

with open("puzzle","r") as infile:
    moves = [(d,int(v)) for line in infile.read().strip().split("\n") for d,v in [line.split()]]

def print_field(positions,save_view=False):
    x_vals = [int(v.real) for v in positions]
    y_vals = [int(v.imag) for v in positions]
    xmin, xmax = min(x_vals)-1, max(x_vals)+1
    ymin, ymax = min(y_vals)-1, max(y_vals)+1
    output = ""
    for y in range(ymin, ymax):
            output += "".join(["s" if x==0 and y == 0 else "#" if complex(x,y) in positions else "."  for x in range(xmin,xmax+1)]) 
            output += "\n"
    
    print(output)
    fid = len(positions)
    if save_view:
        with open(f"fieldview.{fid}","w") as outfile:
            outfile.write(output)
            
directions = {'R':1,
              'L':-1,
              'U':-1j,
              'D':1j}

distance = lambda p1, p2: (p1-p2).real**2 + (p1-p2).imag**2 

def rope_walker(part):
    position = {nr:0 for nr in range(10)}
    visited_positions = {nr:set([0]) for nr in range(10)}
    
    part_factor = {"Part1":1,
                   "Part2":9}[part]
    
    active_knots = list(range(1+part_factor))
    
    for d,v in moves:
        for steps in range(v):
            position[0] += directions[d]
            
            visited_positions[0].add(position[0])
            
            for k_lead,k_follow in zip(active_knots,active_knots[1:]):
                tails_diff = position[k_lead] - position[k_follow]
                if abs(tails_diff.real) > 1 or abs(tails_diff.imag)>1:
                    
                    position[k_follow] = sorted([ (distance(position[k_lead], position[k_follow] + complex(dx,dy)), position[k_follow] +complex(dx,dy))  for dx in [-1,0,1] for dy in [-1,0,1] ],key=itemgetter(0))[0][1]
                    
                    visited_positions[k_follow].add(position[k_follow])
    return visited_positions[part_factor]
      
for part in ["Part1","Part2"]:
    path = rope_walker(part)    
    print(f"{part}: ", len(path))
    print_field(path,True)
