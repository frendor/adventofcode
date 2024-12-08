#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:44:57 2024

@author: frendor
"""
import re

def read_input(puzzle_file):
    with open(puzzle_file,"r") as infile:
        data = infile.read()
    return data
    
def teil1(puzzle_file, debug=False):
    product = 0
    data = read_input(puzzle_file)
    res = re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)",data)

    for result in res:
        f1,f2 = result[:-1].replace("mul(","").split(",")
        if debug: print(f"{result} : {f1} * {f2} = {int(f1)*int(f2)}")
        product += int(f1)*int(f2)
    return product

def teil2(puzzle_file, debug=False):
    product = 0
    data = read_input(puzzle_file)
    res = re.findall(r"(mul\([0-9]{1,3}\,[0-9]{1,3}\))|(don't)|(do)",data)
    if debug:
        print(res)
    skip_mul = False
    for result in res:
        if "don't" in result[1]:
            skip_mul = True
        elif "do" in result[2]:
            skip_mul = False
        if 'mul' in result[0] and not skip_mul:    
            f1,f2 = result[0][:-1].replace("mul(","").split(",")
            if debug:
                print(f"{result} : {f1} * {f2} = {int(f1)*int(f2)}")
            product += int(f1)*int(f2)
    return product

    
if __name__ == "__main__":
    for l in ["example2","input_day3"]:
        print(f"Tag3: {l} - Teil 1: ", teil1(l,debug={"example2":True,"input_day3":False}[l]) )
        print(f"Tag3: {l} - Teil 2: ", teil2(l,debug={"example2":True,"input_day3":False}[l]) )
