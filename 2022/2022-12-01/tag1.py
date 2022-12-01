#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:28:00 2022

@author: frendor
"""


with open("puzzle_input","r") as infile:
    data = infile.read()

#part1:    
elf_total_calories = [sum([int(line) for line in block.split("\n") if line ]) for block in data.split("\n\n")]
print(f"Part1: Elf #{1+elf_total_calories.index(max(elf_total_calories))} carries {max(elf_total_calories)} calories")
    
#part2:
print(f"Part2: Top 3 calory carrier carry {sum(sorted(elf_total_calories)[-3:])}")