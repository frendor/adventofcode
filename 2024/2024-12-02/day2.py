#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:44:57 2024

@author: frendor
"""

def read_lists(puzzle_file):
    with open(puzzle_file,"r") as infile:
        data = [[int(nr) for nr in line.split()] for line in infile.readlines()]        
    return data

test_report = lambda report: all([(e1<e2 and e2-e1 < 4) for e1,e2 in zip(report,report[1:]) ]) or \
                             all([(e1>e2 and e1-e2 < 4) for e1,e2 in zip(report,report[1:]) ])

def part1(puzzle_file):    
    return sum([test_report(line) for line in read_lists(puzzle_file)])

def part2(puzzle_file):
    report_count = 0
    for report in read_lists(puzzle_file):
        skip_index = 0

        while skip_index < len(report):
            if test_report(report[:skip_index]+report[skip_index+1:]):
                report_count +=1 
                break
            skip_index += 1
    return report_count

if __name__ == "__main__":
    for puzzle in ["example","input_day2"]:
        print(f"Part1 {puzzle}: ", part1(puzzle) )
        print(f"Part1 {puzzle}: ", part2(puzzle) )