#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:30:28 2020

@author: frendor
"""

DAY = 6
DEBUG = False

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"


def load_input(filename = PUZZLE ):
    with open(filename,"r") as file:
        input_list = file.read().split("\n\n")
        group_answers = [group.split("\n") for group in input_list]
    return group_answers

def count_different_answers_part1(group_answers):
    total_answers = sum([len(set("".join(answer_set))) for answer_set in group_answers])
    print(f"Part1: Gesamtanzahl von Antworten {total_answers}")

def count_answers_part2(group_answers):
    count_common_answers = 0 
    for answer_set in group_answers:    
        for char in answer_set[0]:
           if all([(char in other_answer) for other_answer in answer_set[1:]]):
               count_common_answers += 1
    print(f"Part2 - Gesamtanzahl von gleichen Gruppenantworten: {count_common_answers}")
    
if __name__ == "__main__":
    group_answers = load_input(PUZZLE)
    count_different_answers_part1(group_answers)
    count_answers_part2(group_answers)