#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 01:56:56 2022

@author: frendor
"""

with open("puzzle","r") as infile:
    data = [[part.strip().replace(",","").split()[-2:] for part in row.split(":")] for row in infile.readlines()]

sensor_beacon_list = [[complex( *[int(p.split("=")[1]) for p in half]) for half in data_set] for data_set in data ]

m_dist = lambda c1,c2: int(abs(c1.real - c2.real) + abs(c1.imag-c2.imag))

def show_field(sensor_beacon_list,covered_area):
    sensor_list, beacon_list = zip(*sensor_beacon_list)

    all_points = set(covered_area).union(set(beacon_list + sensor_list))
    x_min = min([int(r.real) for r in all_points])-1
    x_max = max([int(r.real) for r in all_points])+1
    y_min = min([int(r.imag) for r in all_points])-1
    y_max = max([int(r.imag) for r in all_points])+1

    output = "".ljust(5)+"╔"+"".center(x_max-x_min+3,"═")+"╗"
    output += "\n"

    for row in range(y_min, y_max+1):
        output += f"{row:4.0f} ║"+"".join(['S' if complex(col,row) in sensor_list else\
                                              'B' if complex(col,row) in beacon_list else\
                                              '#' if complex(col,row) in covered_area else\
                                              ' ' for col in range(x_min-1,x_max+2)])+"║"
        output += "\n"
    output += "".ljust(5)+"╚"+"".center(x_max-x_min+3,"═")+"╝"
    output += "\n"
    return output


def line_coverage(c1,c2, distance, target = 2_000_000):    
    if abs(c1.imag - target) <= distance:      
        dy =  target - c1.imag
        range_x = int((distance - abs(dy)))

        l1 = [c1+complex(dx,dy) for dx in range(-range_x,range_x+1) 
                                 if abs(dx) + abs(dy) <= distance
                                 if c1.imag + dy == target]
        return l1
    else:
        return [ ]

diamond_edge = lambda c1, distance, limit: [ c1 + complex((dr)*dx,(distance+1-dr)*dy)  
                                                          for dr in range(0,distance+2)
                                                          for dx in [-1,1]
                                                          for dy in [-1,1]
                                                          if 0 <= (c1 + complex((dr)*dx,(distance+1-dr)*dy)).real<=limit
                                                          and 0 <= (c1 + complex((dr)*dx,(distance+1-dr)*dy)).imag<=limit]

is_inside = lambda p, c1, c2: m_dist(p,c1) <= m_dist(c1,c2)    

def find_lost_beacon(sensor_beacon_list):
    
    if len(sensor_beacon_list) == 14:
        limit = 20  # example
    else:
        limit = 4_000_000 # puzzle
    
    possible_points = set()    
    
    for p1,p2 in sensor_beacon_list:
        d = set([point for point in diamond_edge(p1, m_dist(p1,p2),limit) 
                 if not any([is_inside(point,n1,n2) for n1,n2 in sensor_beacon_list]) ])
        possible_points.update(d)
        if d:
            break # there is only one point inside the field
    if limit == 20:  # show only the example
        print(show_field(sensor_beacon_list, possible_points)    )

    for p in possible_points:
        print ("Part2: Lost beacon tuning frequency: ", int(p.real) * 4000000 + int(p.imag))

### Part1
sensor_list, beacon_list = zip(*sensor_beacon_list)
target_line = set([ p for p1,p2 in sensor_beacon_list for p in line_coverage(p1,p2,m_dist(p1,p2),target=10) if p not in beacon_list])
print(f"Part1: {len(target_line)}")
### Part2:
find_lost_beacon(sensor_beacon_list)