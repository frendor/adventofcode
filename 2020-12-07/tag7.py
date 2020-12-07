#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:30:28 2020

@author: frendor
"""

import re
import numpy as np 

DAY = 7
DEBUG = False

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
    

def load_input(filename = PUZZLE ):
    with open(filename,"r") as file:
        bag_rules = [line.strip().split(" bags contain ") for line in file.readlines()]
        bag_dict = dict([(key,np.array(re.findall(r"([0-9]) ([a-zA-Z ]*) bag|bags*", content))) for key,content in bag_rules] )
        
    return bag_dict 
    
def iter_bags_part1(bag_color,bag_dict):
    bag_content = bag_dict[bag_color].transpose()[1]
    return any([True if next_bag_color == "shiny gold" or (next_bag_color!="" and iter_bags_part1(next_bag_color,bag_dict)) else False for next_bag_color in bag_content])

def iter_bags_part2(bag_color,bag_dict, debug=DEBUG):    
    result = sum([int(nr)*(1+ iter_bags_part2(next_bag_color,bag_dict)) if nr.isnumeric() else 0 for nr, next_bag_color in bag_dict[bag_color] ])
    
    if debug:
        print(bag_color, bag_dict[bag_color], result)

    return result

def part1_find_gold_bag_container(bag_dict,debug=DEBUG):
    good_container = 0
    for bag_container in bag_dict.keys():
        if debug:
            print(bag_container)        
        good_bag = iter_bags_part1(bag_container,bag_dict)
        good_container+= 1 * good_bag 
    return good_container

def part2_bags_shiney_gold(bag_dict):
    return iter_bags_part2("shiny gold",bag_dict)


        
if __name__ == "__main__":
    bag_rules = load_input(PUZZLE)
    print("Part1: Amout of possible bags: ",part1_find_gold_bag_container(bag_rules))
    print("Part2: Bags in shiny gold: ",iter_bags_part2("shiny gold",bag_rules))