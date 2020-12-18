#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:09:08 2020

@author: frendor
"""

DAY = 17

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"

def load_input(filename = EXAMPLE ):
    with open(filename,"r") as file:
        pocket_state = {(x,y):char=="#" for x,line in enumerate(file.readlines()) for y,char in enumerate(line.strip())}
    return pocket_state

def nearby_cubes(pocket_state, position,wdim=False):
    x,y,z,w = position
    return {(dx,dy,dz,wdim*dw):pocket_state.setdefault((dx,dy,dz,wdim*dw),False) for dx in range(x-1,x+2)
                                                                    for dy in range(y-1,y+2) 
                                                                    for dz in range(z-1,z+2)
                                                                    for dw in range(w-1,w+2)
                                                                       if any([(x-dx),(y-dy),(z-dz),wdim*(w-dw)])}

def cycle_pocket_state(pocket_state, wdim=False):
    if len(list(pocket_state.keys())[0]) == 2:
        #Initial 2d input found, expanding to 4d
        pocket_state = {(pos[0],pos[1],0,0):c_state for pos, c_state in pocket_state.items()}
    
    active_positions = [position for position,state in pocket_state.items() if state ]
    xrange, yrange, zrange, wrange = [range(min(vals)-1,max(vals)+2) for vals in zip(*active_positions)]
    next_pocket_state = {(x,y,z,wdim*w):False for x in xrange for y in yrange for z in zrange for w in wrange}

    for position in next_pocket_state.keys():
        if pocket_state.setdefault(position,False):
            next_pocket_state[position] = (sum(nearby_cubes(pocket_state,position,wdim).values()) in [2,3])
        else:
            next_pocket_state[position] = (sum(nearby_cubes(pocket_state,position,wdim).values()) == 3)
            
    return next_pocket_state

def six_cycle_boot(state,wdim=False):
    for cyclenr in range(1,7):
        state = cycle_pocket_state(state,wdim)
    print(f"Part{1+wdim*1}: After the boot {list(state.values()).count(True)} cubes are active") 

        
if __name__ == "__main__":
    state = load_input(PUZZLE)
    six_cycle_boot(state,wdim=False)
    six_cycle_boot(state,wdim=True)