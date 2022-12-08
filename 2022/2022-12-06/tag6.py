#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:23:16 2022

@author: frendor
"""

with open("puzzle","r") as infile:
    data = [line.strip() for line in infile.readlines()]
    
def get_marker(signal,different_chars=4):
    for pos in range(len(signal)-different_chars):        
        if len(set(signal[pos:pos+different_chars])) == different_chars:
            return pos+different_chars
        
        
for part in [1,2]:
    different_chars = {1:4,
                       2:14}[part]        
    print(f" Part{part} ".center(20,"#"))
    for line in data:
        marker = get_marker(line,different_chars)
        print(line,marker)
    