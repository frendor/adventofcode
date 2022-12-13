#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:24:09 2022

@author: frendor
"""

from functools import reduce
mal = lambda a,b: a*b

class Monkey(object):
    def __init__(self, name, items, operation, test, yes, no, part):
        self.name = name.strip()[:-1]
        self.items = [int(elem.strip()) for elem in items.strip().replace("Starting items: ","").split(",")]
        op1 = operation.replace('Operation: new = old ',"").strip() 
        self.operation = (int(op1.replace("+ ","")) if "+" in op1 else False, 
                          int(op1.replace("* ","")) if "*" in op1 and "old" not in op1 else False,
                          "* old" in op1)
        self.test = int(test.replace("Test: divisible by ","").strip())
        self.yes = int(yes.strip().replace("If true: throw to monkey ",""))
        self.no = int(no.strip().replace("If false: throw to monkey ",""))        
        self.counter = 0
        self.common_divisible = 1
        self.part = {"Part1":lambda value: value//3,
                     "Part2":lambda value: value%self.common_divisible}[part] 
    
    def give_item(self,item):
        self.items.append(item)
      
    def juggle(self):
        for item in self.items:
            new_value = self.inspect(item)
            to_monkey = self.test_item(new_value)
            monkey_list[to_monkey].give_item(new_value)
        self.items = []
            
    def inspect(self, item):
        self.counter += 1
        for nr, val in enumerate(self.operation):
            if nr == 0 and val:
                new_item = item + val
            elif nr == 1 and val:
                new_item = item * val
            elif nr == 2 and val:
                new_item = item * item        
        return self.part(new_item)
    
    def test_item(self,item):
        if item% self.test == 0:
            return self.yes
        else:
            return self.no
 
    def __repr__(self):
        return self.name
    
    def __str__(self):    
        return self.name
    

with open("puzzle") as infile:
    data = infile.read().strip()

show_infos = False
for part in ["Part1", "Part2"]:
    monkey_list = [Monkey(*monkey.split("\n"),part) for nr,monkey in enumerate(data.split("\n\n"))]    
    common_divisible = reduce(mal,[monkey.test for monkey in monkey_list])
    for monkey in monkey_list:
        monkey.common_divisible = common_divisible

    for iteration in range(1,{"Part1":21,
                              "Part2":10001}[part]):
        for monkey in monkey_list:
            monkey.juggle()
        if (iteration in [1,20] or iteration%1000 == 0) and show_infos:
            print(f" Round {iteration} ".center(30,"-"))
            for monkey in monkey_list:
                print(f"{monkey.name:8s} | {monkey.counter:7.0f} | {','.join([str(elem) for elem in monkey.items])}")
    
    
    for p1,p2 in (sorted([monkey.counter for monkey in monkey_list],reverse=True)[:2],):
        print(f"{part}: Monkey business {p1*p2} ")
        print()
