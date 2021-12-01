#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:21:59 2020

@author: frendor
"""

import re

DAY = 18

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"

def load_input(filename = EXAMPLE ):
    with open(filename,"r") as file:
        math_list = [line.strip() for line in file.readlines()]
    return math_list


def eval_match(m):
    if m.group("term"):
        return str(eval(m.group("term")))


def recursive_eval(match,adv=False):
    match_line = match.group('term')

    if re.search(r"\((?P<term>[\d*+ ]+)\)",match_line):
        prev_line = ""
        while prev_line is not match_line:
            prev_line = match_line
            match_line = re.sub(r"\((?P<term>[\d*+ ]+)\)",lambda term: recursive_eval(term,adv) , match_line)
        
    prev_line = ""
    while prev_line is not match_line: 
        prev_line = match_line
        if adv:
            match_line = re.sub(r"(?P<term>\d+ \+ \d+)",eval_match, match_line,count=1)
        else:
            match_line = re.sub(r"(?P<term>\d+ [+,*] \d+)",eval_match, match_line,count=1)

    prev_line = ""
    while prev_line is not match_line: 
        prev_line = match_line
        match_line = re.sub(r"(?P<term>(\d+ \* )+\d+)",eval_match, match_line,count=1)

    return match_line


def evaluate_adv_list(math_list,adv):
    total_sum = 0
    for math_line in math_list:
        math_line = re.sub(r"(?P<term>.*)",lambda term: recursive_eval(term,adv), math_line)
        total_sum += int(math_line)
    return total_sum
    

if __name__ == "__main__":
    math_list = load_input()
    total_sum = evaluate_adv_list(math_list, adv=False)
    print("Part1: Sum of all lines ",total_sum)
    total_sum = evaluate_adv_list(math_list, adv=True)
    print("Part2: Sum of all lines ",total_sum)