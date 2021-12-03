#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:28:42 2021

@author: frendor
"""

import numpy as np

with open("t3input","r") as file:
    bits = np.array([list(line.strip()) for line in file.readlines()])


#part1
gamma_list = [1 if list(bit).count('1')/float(len(bit))>0.5 else 0 for bit in bits.transpose()]
ep_list = [0 if list(bit).count('1')/float(len(bit))>0.5 else 1 for bit in bits.transpose()]

mk_bin = lambda zahl_list: int("0b"+ "".join([str(char) for char in zahl_list]),2)

gamma = mk_bin(gamma_list)
ep = mk_bin(ep_list)

print(f"Part1: Gamma: {gamma} Epsilon: {ep} Rating: {gamma*ep} ")

#part2:
get_O2_selector = lambda bitlist:  1 if np.array(bitlist,dtype=int).sum()/float(len(bitlist))>=0.5 else 0
get_CO2_selector = lambda bitlist:  1 if np.array(bitlist,dtype=int).sum()/float(len(bitlist))<0.5 else 0

def iterate_rate(bits, selector_function):
    new_bits = bits[:]
    for step,value in enumerate(new_bits[0]):
        bit_selector = selector_function(new_bits.transpose()[step])
        new_bits = np.array([line for line in new_bits if bit_selector == int(line[step])])
        if len(new_bits) == 1:
            break
    return(new_bits[0])

O2_rate = "".join(iterate_rate(bits, get_O2_selector))
CO2_rate = "".join(iterate_rate(bits, get_CO2_selector))

print(f"Part2: O2: {mk_bin(O2_rate)}, CO2: {mk_bin(CO2_rate)}, Solution: {mk_bin(CO2_rate)*mk_bin(O2_rate)}")
