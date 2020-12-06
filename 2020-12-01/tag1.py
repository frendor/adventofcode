#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:30:25 2020

@author: frendor
"""

expanse_file = "expanse.list"

with open(expanse_file,"r") as file:
    values = [int(val) for val in file.readlines()]
    
for nr,val1 in enumerate(values):
    run = [val1 * val2 for val2 in values[nr+1:] if val1+val2 == 2020]
    if run:
       print("Teil1: ",run)
       break

for nr1,val1 in enumerate(values):
    for nr2,val2 in enumerate(values[nr1+1:]):
        run = [val1 * val2 * val3 for val3 in values[nr2+nr1:] if val3+val1+val2 == 2020]
        if run:
            print("Teil2: ",run)
            break
    
if __name__=="__main__":
    pass