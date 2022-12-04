#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:16:51 2022

@author: frendor
"""
import numpy as np

build_set = lambda pair: set(list(range( *(np.array(pair.split("-"),dtype=int) + [0,1]) )))

with open("puzzle","r") as infile:
    data = [ (build_set(p1),build_set(p2)) for line in infile.readlines() for p1,p2 in [ line.strip().split(",") ]]
        
print("Part1: ", sum([1 for s1,s2 in data if s1.issubset(s2) or s2.issubset(s1)]))
print("Part2: ", sum([1 for s1,s2 in data if s1.intersection(s2)]))