#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 02:56:47 2022

@author: frendor
"""

with open("puzzle","r") as infile:
    data = [line.strip() for line in infile.readlines()]

x_dim = len(data[0])
y_dim = len(data)
max_dim = max(x_dim, y_dim)
                
field = {}
for y,line in enumerate(data):
    for x,val in enumerate(line):
        field[complex(x,y)] = int(val)
        
get_lines = lambda pos: [ [field[pos + ds*step] for step in range(1,max_dim) if pos+ds*step in field ]  for ds in [1,-1,1j,-1j]] 
check_line = lambda pos, line: all([field[pos]>tree for tree in line])
check_all_lines = lambda pos: any([check_line(pos,line) for line in get_lines(pos) ])

print("Part1:",sum([check_all_lines(position) for position in field.keys()]))

def visible_trees(pos, ds):
    height = field[pos]
    step = 1*(pos + ds in field)

    while pos + ds*(step+1) in field and field[pos+ds*(step)] < height:
        step +=1            
        
    return step

count_trees = lambda pos: [visible_trees(pos,ds) for ds in (1,-1,1j,-1j)]

def scenic_score(trees):
    score = trees[0]
    for t in trees[1:]:
        score = score*t
    return score

print("Part2: Best Scenic Score:", max([scenic_score(count_trees(pos)) for pos in field.keys()]))