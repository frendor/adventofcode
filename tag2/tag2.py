#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:30:25 2020

@author: frendor
"""

DAY = 2
DEBUG = False
PUZZLE_FILE = f"t{DAY}puzzle.input"

with open(PUZZLE_FILE,"r") as file:
    pass_list = []
    for line in file.readlines():
        fullrule,passwd = line.split(": ")
        pwrange, req_char = fullrule.split(" ") 
        low_range, high_range = [int(number) for number in pwrange.split("-")]
        passwd = passwd.strip()
        pass_list.append((low_range, high_range,req_char,passwd))
    
    p1_valid_passwords = 0
    p2_valid_passwords = 0
    #Part1
    for  lo_r,hi_r, req_char, pw in pass_list:
        if lo_r <= pw.count(req_char) <= hi_r:
            p1_valid_passwords += 1
            if DEBUG:
                print("Ok: ",pw)
        else:
            if DEBUG:
                print("Not OK: ", pw)
    print("Part1 - valids Passwords: ",p1_valid_passwords)
    
    #Part2
    for  lo_r,hi_r, req_char, pw in pass_list:
        if (pw[lo_r-1] == req_char or pw[hi_r-1] == req_char)\
           and not (pw[lo_r-1] == req_char and pw[hi_r-1] == req_char):
            p2_valid_passwords += 1
            if DEBUG:
                print(f"Ok: {lo_r}-{hi_r} {req_char}:{pw}" )
        else:
            if DEBUG:
                print("Not OK: ", pw)
    print("Part2 - valids Passwords: ",p2_valid_passwords)
    
    
if __name__=="__main__":
    pass