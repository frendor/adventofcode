#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:55:32 2020

@author: frendor
"""

import numpy as np

DAY = 12

VERBOSE = True

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
EXAMPLE2 = f"t{DAY}puzzle.example2"

def load_input(filename = PUZZLE ):
    with open(filename,"r") as file:
        nav_list = [line.strip() for line in file.readlines()]
    return nav_list 

co = lambda ang: np.cos(np.radians(ang))
si = lambda ang: np.sin(np.radians(ang))
rot_mat = lambda ang: np.array([[co(ang), -si(ang)],[si(ang), co(ang)]])


def position(nav_list):
    face_dir = np.array([0.,1.])
    position = np.array([0.,0.])
    directions = {'N':np.array([1.,0.]),
                  'E':np.array([0.,1.]),
                  'S':np.array([-1.,0.]),
                  'W':np.array([0.,-1.])}
    rotations = {"R":-1.,
                 "L":1.}    
    
    for nr,order in enumerate(nav_list):
        action = order[0]
        arg = int(order[1:])
        if action in directions:
            position += arg * directions[action]
        if action in rotations:
            print(face_dir, order, end="")
            face_dir = np.matmul(face_dir , np.round(rot_mat(rotations[action]* arg )))
            print(face_dir)
        if action == "F":
            
            position += face_dir * arg
        print(f"{nr}: {order} and ends at {position}")
        
    return position

def waypoint(nav_list):
    waypoint = np.array([1.,10.])
    position = np.array([0., 0.,])
    directions = {'N':np.array([1.,0.]),
                  'E':np.array([0.,1.]),
                  'S':np.array([-1.,0.]),
                  'W':np.array([0.,-1.])}
    rotations = {"R":-1.,
                 "L":1.}    
    for nr,order in enumerate(nav_list):
        action = order[0]
        arg = int(order[1:])
        if action in directions:
            waypoint += arg * directions[action]
        if action in rotations:
            print(waypoint, order, end="")
            waypoint = np.matmul(waypoint , np.round(rot_mat(rotations[action]* arg )))
            print(waypoint)
        if action == "F":
            position += waypoint * arg
        print(f"{nr}: {order} and ends at {position}")
    return position
    
    
man_dist = lambda pos: np.sum(np.abs(pos))
print_pos = lambda pos: "{0}{1:.0f} {2}{3:.0f}".format({1.:"N",-1.:"S"}[round(pos[0]/abs(pos[0]))],
                                           abs(pos[0]),
                                           {1.:"E",-1.:"W"}[round(pos[1]/abs(pos[1]))],
                                           abs(pos[1]))

if __name__ == '__main__':
    nav_list = load_input()
    pos = position(nav_list)
    print(f"Part1: new Position is {print_pos(pos)}. Manhattan Distance is {man_dist(pos):.0f}.")
    pos_part2 = waypoint(nav_list)
    print(f"Part1: new Position is {print_pos(pos_part2)}. Manhattan Distance is {man_dist(pos_part2):.0f}.")