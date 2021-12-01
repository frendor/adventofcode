#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:20:49 2020

@author: frendor
"""

DAY = 14

VERBOSE = False

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
EXAMPLE2 = f"t{DAY}puzzle.example2"

def load_input(filename = EXAMPLE ):
    with open(filename,"r") as file:
        input_list = [line.strip() for line in file.readlines()]
    return input_list 

def parse_mask(mask):
    mask_dict = {'1':[],
                 '0':[],
                 'X':[]}    
    for bitnr,char in enumerate(reversed(list(mask))):
        if char in ['0','1','X']:
            mask_dict[char].append(bitnr)
    return mask_dict

def setbit(value, position):
    return (value | 1 << position)
     
def clearbit(value, position):
    return (value & ~(1 << position ))
    
def mask_version_v1(integer, mask,verbose=VERBOSE):
    if verbose:
        print(f"before maskv1: {integer} with mask {mask}")

    for pos in mask['1']:
        integer = setbit(integer,pos)    
    for pos in mask['0']:
        integer = clearbit(integer,pos)

    if verbose:
        print("MaskV1 applied: ",integer)
    return integer

def mask_version_v2(address, mask,verbose=VERBOSE):
    if verbose:
        print(f"before maskv2: {address} with mask {mask}")

    for pos in mask['1']:
        address = setbit(address,pos)
    
    addr_list = [address]
    for pos in mask['X']:
        addr_list = [fkt(value,pos) for value in addr_list for fkt in [setbit, clearbit]]        
    if verbose:
        print("MaskV2 applied: ",addr_list)
        
    return addr_list

    
def part1_mask_memory(input_list):
    memory = {}
    for line in input_list:
        if line[:3] == "mas":
            mask = parse_mask(line)
        if line[:3] == "mem":
            mem, value = line.replace('mem[',"").split( "] = ")
            memory.setdefault(mem,0)
            value = mask_version_v1(int(value),mask)
            memory[mem]=value
    print(f"Part1: {sum(memory.values())}") 


def part2_mask_address(input_list):
    memory = {}
    for line in input_list:
        if line[:3] == "mas":
            mask = parse_mask(line)
        if line[:3] == "mem":
            mem, value = line.replace('mem[',"").split( "] = ")
            address_list = mask_version_v2(int(mem),mask)
            for address in address_list:    
                memory.setdefault(address,0)            
                memory[address]=int(value)
    print(f"Part2: {sum(memory.values())}") 
    
    
if __name__=="__main__":
    input_list = load_input(PUZZLE)
    
    part1_mask_memory(input_list)
    part2_mask_address(input_list)