#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:28:42 2021

@author: frendor
"""

def loadfile(filename="t2example"):
    with open(filename,"r") as file:
        commands = [line.split() for line in file.readlines()]
    return commands

def part1(commands):
    command_dict = {"forward":1,
         "down":1j,
         "up":-1j}
    position= sum([command_dict[step] * int(size) for step, size in commands])
    print(f"Part1: Forward: {position.real}, Depth: {position.imag}, Solution: {position.real*position.imag}")
    
def part2(commands):
    command_dict = {"forward":1,
         "down":1j,
         "up":-1j}
    position = 0
    aim = 0 
    for step, size in commands:
        current_step = command_dict[step] * int(size)
        aim += current_step
        position += current_step.real + (current_step.real * aim.imag )*1j
    print(f"Part2: Forward: {position.real}, Depth: {position.imag}, Aim: {aim.imag}, Solution: {position.real * position.imag}")
    
print("Example:")
part1(loadfile())
part2(loadfile())
print("Puzzle:")
part1(loadfile("t2input"))
part2(loadfile("t2input"))