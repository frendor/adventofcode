#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:28:42 2021

@author: frendor
"""

def loadfile(filename="t1example"):
    with open(filename,"r") as file:
        data = [int(value) for value in file.read().split("\n")]
    return data

def part1(inputdata):
    counts = 0
    for nr,value in enumerate(inputdata[1:]):
        counts += (inputdata[nr] < value) * 1
        #print(f"{inputdata[nr]} < {value} : {(inputdata[nr] < value) * 1}")
    return counts
    

def part2(inputdata):
    counts = 0
    for nr,value in enumerate(inputdata[3:]):
        counts += (sum(inputdata[nr:nr+3]) < sum(inputdata[nr+1:nr+4]))*1
        #print("{}+{}+{} = {} <({}) {} = {}+{}+{}".format(*inputdata[nr:nr+3],sum(inputdata[nr:nr+3]),(sum(inputdata[nr:nr+3])<sum(inputdata[nr+1:nr+4]))*1 ,sum(inputdata[nr+1:nr+4]),*inputdata[nr+1:nr+4]))
    return counts

print("Beispiel:")
print(f"Part 1: So oft wird es tiefer: {part1(loadfile('t1example'))}") 
print(f"Part 2: So oft wird es tiefer: {part2(loadfile('t1example'))}")
#
print("Puzzle:")
print(f"Part 1: So oft wird es tiefer: {part1(loadfile('t1puzzle'))}") 
print(f"Part 2: So oft wird es tiefer: {part2(loadfile('t1puzzle'))}") 

 