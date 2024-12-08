#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:01:55 2024

@author: frendor
"""

word = "XMAS"
    
def read_input(filename):
    with open(filename,"r") as infile:
        data =  infile.read().strip()
    return data

def print_p1_solution(lines, sol_list):
    good_points = [(line_at+base[0]*pos,col_at+base[1]*pos) for line_at, col_at, base in sol_list for pos, char in enumerate(word)] 
    row_count = len(lines)
    col_count = len(lines[0])
    print ( "\n".join( [ "".join(["." if not (r,c) in good_points else lines[r][c] for c in range(col_count) ]) for r in range(row_count)]) )

def show_p2_solutions(lines, sol_list):
    good_points = [(line_at+d1,col_at+d2) for line_at, col_at in sol_list for d1 in [-1,0,1] for d2 in [-1,0,1] if d1==d2==0 or abs(d1) == abs(d2) == 1] 
    row_count = len(lines)
    col_count = len(lines[0])
    print ( "\n".join( [ "".join(["." if not (r,c) in good_points else lines[r][c] for c in range(col_count) ]) for r in range(row_count)]) )


def find_word(lines,line_at,col_at):
    row_count = len(lines)
    col_count = len(lines[0])
    sol_list = []
    count = 0
    for base in [(x,y) for x in [-1,0,1] for y in [-1,0,1] if y**2+x**2>0 ]:
        res = all([0 <= col_at + base[1]*pos <col_count and 0<= line_at + base[0]*pos < row_count and letter == lines[line_at + base[0]*pos][col_at + base[1]*pos]  for pos, letter in enumerate(word) ])
        
        if res:
           sol_list.append([line_at, col_at, base])
           count+=1 
    return count, sol_list   

def find_solutions(input_file,debug=False):
    data = read_input(input_file)

    lines = data.split("\n")

    sol_list = []
    
    solutions = 0 
    for line_nr, line in enumerate(lines):
        for col_nr, char in enumerate(line):
            if char == "X":
                count,sols = find_word(lines,line_nr,col_nr)
                sol_list.extend(sols)
                solutions += count
    if debug: 
        print_p1_solution(lines,sol_list)
    return solutions


def is_solution(lines,line_at,col_at, debug=False):
    row_count = len(lines)
    col_count = len(lines[0])
    diag1 = [(+1,+1),(-1,-1)]
    diag2 = [(+1,-1),(-1,+1)]
    good_diag_found=[False,False]
    for nr,diag in enumerate((diag1,diag2)):
        for c1,c2 in [("M","S"),("S","M")]:
            if (0<=diag[0][0]+line_at<row_count and 
                0<=diag[0][1]+col_at < col_count and 
                0<=diag[1][0]+line_at<row_count and 
                0<=diag[1][1]+col_at < col_count and 
                    
                lines[diag[0][0]+line_at][diag[0][1]+col_at] == c1 and
                lines[diag[1][0]+line_at][diag[1][1]+col_at] == c2) :
                good_diag_found[nr] = True

    return all(good_diag_found)
             

def find_solutions_p2(input_file, debug=False):
    data = read_input(input_file)

    lines = data.split("\n")
    sol_list = []

    for line_nr, line in enumerate(lines):
        for col_nr, char in enumerate(line):
            if char == "A":
                res = is_solution(lines,line_nr,col_nr, debug)
                if res:
                    sol_list.append([line_nr,col_nr])
    if debug: 
        show_p2_solutions(lines,sol_list)
    return len(sol_list)
   

if __name__ == "__main__":
    for puzzle in ["example","input_day4"]:
        show_debug = {"example":True,
                      "input_day4":False}[puzzle]
        print(f"Part1 {puzzle}: ", find_solutions(puzzle,show_debug) )
        print(f"Part2 {puzzle}: ", find_solutions_p2(puzzle,show_debug) )
        
        
        
