#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 15:20:01 2022

@author: frendor
"""

with open("puzzle","r") as infile:
    commands = infile.read().strip().split("\n")
    

def execute_program(commands):
    display  = ""
    signal_output = ""
    task_list = {}
    x = 1
    cycle = 1
    signal_sum = 0
    
    while commands or task_list:
        if cycle%40 == 20:
            signal_strength = cycle * x            
            #signal_output += f"{cycle:3.0f} | {x:3.0f} | with signal strength {signal_strength}\n" 
            signal_sum += signal_strength
        
        if (cycle-1)%40 == 0:
            display+="\n"
        
        if x-1 <= (cycle-1)%40 <= x+1:
            display += "█"
        else:
            display += " "
            
        if cycle in task_list:
            task = task_list.pop(cycle)
            if isinstance(task,int):
                x += task
        else:
            order = commands.pop(0)
            
            if order.startswith("addx"):
                task_list[cycle+1] = int(order.split()[1])
    
        cycle += 1
    
    print(" Part1 ".center(20,"-"))
    print(f"Part1: Signal Sum {signal_sum}")    
    print(signal_output)

    print(" Part2 ".center(20,"-"))
    print(display)    
    
execute_program(commands)