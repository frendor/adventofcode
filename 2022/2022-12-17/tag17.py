#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:02:00 2023

@author: frendor
"""

with open("puzzle","r") as infile:
    pattern = infile.read().strip()

pat_len = len(pattern)
jet_shift_list = [1 if char == ">" else -1 for char in pattern]

rock_1 = [0,1,2,3]
rock_2 = [1,1j,1+2j,2+1j]
rock_3 = [0,1,2,2+1j,2+2j]
rock_4 = [0,1j,2j,3j]
rock_5 = [0,1,1j,1+1j]

shapes = [rock_1,rock_2,rock_3,rock_4,rock_5]

def print_shape(shape,stack= set() ,offset=2+3j):
    output = ""
    shifted_shape = [offset+ elem for elem in shape]
    max_height = int(max([elem.imag for elem in stack.union(set(shifted_shape))]))
    for row_nr in range(1+max_height):
        line = "│"+ "".join(['@' if complex(nr,row_nr) in set(shifted_shape) else \
                             '#' if complex(nr,row_nr) in stack else\
                             "." for nr in range(7)]) +"│"
        # █
        output = line+"\n" + output
    output += "╰"+"".center(7,"─")+"╯\n"
    print(output)
    return output

def rock_tower(part):

    tower_state = [0 for elem in range(7)]
    
    shape_counter = 0
    pat_counter = 0
    tower_height = 0
    tower = set()
    
    state_lib = {}
    first_hit = False
    hit_dict = {}
    target = {"Part1":2022,
              "Part2":1000000000000}[part]
    rest_counter = False
    add_tower_height = 0
    
    while shape_counter <= target - 1:
        next_shape = shapes[shape_counter%5]
    
        offset = 2 + jet_shift_list[pat_counter%pat_len] + 3j + tower_height 
        shape_coords = [offset + elem for elem in next_shape]
        pat_counter +=1
        
        still_falling = True
        while still_falling:
            for shift in (-1j, jet_shift_list[pat_counter%pat_len] ):
    
                next_shape_coords = set([coords +shift for coords in shape_coords ])
                if shift.imag == 0:
    
                    pat_counter +=1
                    if next_shape_coords.isdisjoint(tower) and all([0 <= coords.real <= 6 for coords in next_shape_coords ]):
                        shape_coords = next_shape_coords    
    
                else:
                    if next_shape_coords.isdisjoint(tower) and all([ coords.imag >= 0 for coords in next_shape_coords ]):
                        shape_coords = next_shape_coords    
    
                    else:
                        tower = tower.union(shape_coords)
                        tower_state = [complex(0,max([c.imag + 1 for c in shape_coords if c.real == col] + [val.imag] )) for col,val in enumerate(tower_state) ]
                        
                        tower_height = complex(0,max([c.imag for c in tower_state]))
                        still_falling = False
                        break
                    
        if (shape_counter%5,pat_counter%pat_len) in state_lib and not rest_counter:
            ### Searching for a unit-cell            
            ts_lowest = complex(0, min([c.imag for c in tower_state]))
            ts_relative = [c - ts_lowest for c in tower_state]
            
            if state_lib[(shape_counter%5,pat_counter%pat_len)]['state'] == ts_relative and not first_hit:
                first_hit = (shape_counter%5,pat_counter%pat_len)
    
            if first_hit and first_hit == (shape_counter%5,pat_counter%pat_len):
                
                if 1 not in hit_dict:
                    hit_dict[1] = shape_counter
                    hit_dict['th1'] = tower_height
                    hit_dict['pc1'] = pat_counter
                elif 2 not in hit_dict:
                    hit_dict[2] = shape_counter
                    hit_dict['th2'] = tower_height
                    hit_dict['pc2'] = pat_counter
                elif 3 not in hit_dict:
                    hit_dict[3] = shape_counter
                    hit_dict['th3'] = tower_height
                    hit_dict['pc3'] = pat_counter            
                
                if 3 in hit_dict:
                    length = hit_dict[2] - hit_dict[1]
                    tower_diff = hit_dict['th2'] - hit_dict['th1']
                    p_diff = hit_dict['pc2'] - hit_dict['pc1']
                    
                    if hit_dict[2] + length == hit_dict[3] and hit_dict['th2']+tower_diff == hit_dict['th3']:
                        
                        repetitions = (target-1 - hit_dict[1])//length  
                        
                        rest = (target-1 - hit_dict[1]) % length
                        add_tower_height = (repetitions-2) * tower_diff
                        print(f"Unitcell with size {tower_diff.imag:.0f} units ({length} rocks) found: Repeat the cell {repetitions}x times, {rest} rocks are missing")
                        new_shape_counter = repetitions * length + hit_dict[1]
                        new_pat_counter = repetitions * p_diff + hit_dict['pc1']
                        print(f"Jump to rock: {new_shape_counter}, PC: {new_pat_counter}" )
                        shape_counter, pat_counter = new_shape_counter, new_pat_counter
                        rest_counter = True
                    else:
                        print("Houston, we have a problem")
                        break
                        
                
        elif (shape_counter%5,pat_counter%pat_len) not in state_lib and not rest_counter:
            t_lowest = complex(0, min([c.imag for c in tower_state]))
            state_lib[(shape_counter%5,pat_counter%pat_len)] = {'state':[c - t_lowest for c in tower_state],
                                                                'scounter': shape_counter,
                                                                'theight':tower_height}
    
        shape_counter +=1    
    print(f"{part}: The tower height is {(add_tower_height+ tower_height).imag:.0f} units, given by {target} rocks")

for p in [f"Part{c}" for c in [1,2]]:
    rock_tower(p)   
