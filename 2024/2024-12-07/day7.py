#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:49:38 2024

@author: frendor
"""

with open("puzzle","r") as infile:
    data=[row.strip().split(":") for row in infile.readlines()]
    

multiply = lambda a,b: a*b
plus = lambda a,b: a+b
concat = lambda a,b : int(str(a)+str(b))
op_dict = {multiply:"x",plus:"+",concat:"||"}

def next_step(result, step_result, flist, op_list):
    if result == step_result and len(flist) == 0:
        return []
    elif result < int(step_result):
        return False
    elif flist == []:
        return False
    
    if result >= step_result: 
        new_factor = flist[0]

        for fkt in op_list:
            fac_list = next_step(result, fkt(step_result,new_factor), flist[1:], op_list)
            if type(fac_list) is list:                
                return [fkt] + fac_list
        return False    

def print_good_eq(result,fkt_list, factors):
    op_list = [op_dict[fkt] for fkt in fkt_list]
    equation = f"{result} = "
    for fac,op in zip(factors,op_list):
        equation += f"{fac} {op} "
    return f"{equation}{factors[-1]}"
    
    

part_sum = [0,0]
for run, extra_operator in enumerate([[] ,[concat]]):
    for nr,(result, eq) in enumerate(data):
        result = int(result)
        factors = [int(no) for no in eq.strip().split()]
        first_factor = factors[0]
        operator_list = [multiply, plus]
        operator_list.extend(extra_operator)
        fkt_list = next_step(result, first_factor, factors[1:], operator_list)
        if fkt_list:
            #print(f" {nr} ok: {print_good_eq(result,fkt_list, factors)}")
            part_sum[run] += result
    print("Teil1: ", part_sum[run])