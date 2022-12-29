#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 02:52:01 2022

@author: frendor
"""

from math import inf
from queue import PriorityQueue

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Cave:
    minute: int
    name: Any=field(compare=False)
    
with open("puzzle","r") as infile:
    data =  [line.strip() for line in infile.readlines()]


flow_rates = {line.split()[1]: int(line.split()[4].replace(";","").split("=")[1]) for line in data}
connections = {line.split()[1]: line.split(";")[1].replace(",","").split()[4:] for line in data}

closed_valves = set([key for key,v in flow_rates.items() if v!=0])


def find_way(start_cave,start_minute=0):
    visited_notes = set()    
    cave_map = {start_cave:(start_minute,"")}
    
    PQ = PriorityQueue()    
    PQ.put(Cave(start_minute,start_cave))
    
    while not PQ.empty():
        ac = PQ.get()
        minute, active_cave = ac.minute, ac.name

        visited_notes.add(active_cave)
        for next_cave in [cave for cave in connections[active_cave] if cave not in visited_notes]:
            cave_map.setdefault(next_cave,(inf,active_cave))
            if cave_map[next_cave][0] > minute+1:
                cave_map[next_cave] = (minute+1,active_cave)
            PQ.put(Cave(minute+1,next_cave))
    return cave_map

distance_dict = {k:find_way(k) for k in connections.keys() }

def get_way(start, dest):
    way = [dest]
    cave_map = distance_dict[start]
    step, last_cave = cave_map[dest]
    step_nr=0
    while step > 0 and step_nr<30:
        way.append(last_cave)
        step, last_cave = cave_map[last_cave]
        step_nr += 1
    return list(reversed(way))

way_dict = {(k,d):get_way(k,d) for k in flow_rates.keys() for d in flow_rates.keys() if d is not k }
 
calc_exhaust = lambda dur,cave, max_minute=30: (max_minute-dur) * flow_rates[cave]

def test_sequence(seq,max_minute=30):
    seq = ["AA"] + list(seq) if "AA" not in seq else seq
    minute = 0
    exhaust = 0

    full_way = []
    for last_cave, active_cave in zip(seq,seq[1:]):
        dauer,_ = distance_dict[last_cave][active_cave]
        way = way_dict[(last_cave,active_cave)] #get_way(cave_map, active_cave)
        full_way.extend( way )
        if minute+dauer >= max_minute:
            break
        minute += dauer + 1
        exhaust += calc_exhaust(minute,active_cave, max_minute)
    return exhaust
        
valve_options = lambda cave_map,minute,closed_valves, max_minute=30: sorted([(minute+cave_map[target_cave][0]+1,
                                                                              -calc_exhaust(cave_map[target_cave][0]+1+minute,
                                                                                            target_cave,
                                                                                            max_minute), 
                                                                              target_cave)  
                                                                            for target_cave in closed_valves
                                                                            if target_cave in cave_map 
                                                                            if minute+cave_map[target_cave][0]+1 <= max_minute  ])
max_exhaust = 0
best_seq = []

def find_sequence(actual_cave, minute, still_closed_valves, current_exhaust=0, visited_caves = [], max_minute=30):
        
    global max_exhaust
    global best_seq 

    if -current_exhaust > max_exhaust and minute <=max_minute:
        
        max_exhaust = -current_exhaust
        best_seq = visited_caves
        #print(f"Besseren exhaust gefunden:{minute} {max_exhaust}: {visited_caves} (Test: {test_sequence(visited_caves,max_minute=max_minute)}")
    else:
        pass

    cm1 = distance_dict[actual_cave]    
    
    options = valve_options(cm1, minute, still_closed_valves,max_minute)
        
    for duration,t_ex, cave in [(duration,t_ex,cave) for duration,t_ex, cave in options if duration + 1 < max_minute]:
        find_sequence(cave, 
                      duration, 
                      still_closed_valves.difference(set([cave])),
                      current_exhaust+t_ex,
                      [c for c in visited_caves+[cave]], max_minute=max_minute)
            

find_sequence("AA",0,closed_valves)
print("Part1: ", max_exhaust, best_seq)

def test_sequence_2_worker(*sequences):
    return sum([test_sequence(s, max_minute=26) for s in sequences])
    
def get_minute(seq):
    seq = ["AA"] + list(seq)
    minute = 0
    for last_cave, active_cave in zip(seq,seq[1:]):
        cave_map = distance_dict[last_cave]
        dauer,_ = cave_map[active_cave]
        minute += dauer + 1

    return minute-1
    
def find_sequence_2_worker(sequences, cv,  current_exhaust  ):
    global max_exhaust
    global best_seq 
    
    seq0, seq1 = sequences
    actual_minute = [get_minute(s) for s in sequences]
    
    if -current_exhaust > max_exhaust:
        best_seq = sequences
        print(f"Besseren exhaust gefunden: {max_exhaust}<{-current_exhaust} {seq0[1:]} {seq1[1:]} ")
        max_exhaust = -current_exhaust
    else:
        pass
    
    ac0,ac1 = [s[-1] for s in sequences]
    
    w0_cavemap = {k:v0 for k,v0 in distance_dict[ac0].items() 
                       for k1,v1 in distance_dict[ac1].items() 
                       if k==k1 if v0[0]+actual_minute[0] <= v1[0]+actual_minute[1]}
    w1_cavemap = {k:v1 for k,v0 in distance_dict[ac0].items() 
                       for k1,v1 in distance_dict[ac1].items() 
                       if k==k1 if v0[0]+actual_minute[0] > v1[0]+actual_minute[1]}

    walker_cavemap = [w0_cavemap,w1_cavemap]
    
    options = [valve_options(cavemap, actual_minute[walker],cv,max_minute=26) for walker,cavemap in enumerate(walker_cavemap)]

    for walker,duration,t_ex, cave in [(walker,*next_cave) for walker, cm in enumerate(options) for next_cave in cm]:
        if walker == 0:
            nseq0 = seq0 + [cave]
            nseq1 = seq1
        else:
            nseq0 = seq0
            nseq1 = seq1 + [cave]

        find_sequence_2_worker([nseq0, nseq1], 
                               cv.difference(set([cave])),
                               current_exhaust+t_ex)

max_exhaust = 0    
print(" Part2 ".center(30,"#"))
find_sequence_2_worker([["AA"],["AA"]], closed_valves, current_exhaust=0)
print("Part2: ", max_exhaust, best_seq)
