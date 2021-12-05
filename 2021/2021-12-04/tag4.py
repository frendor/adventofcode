#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:28:42 2021

@author: frendor
"""

import numpy as np

with open("t4input","r") as file:
    called_numbers = [int(number) for number in file.readline().strip().split(",")]
    fields = [np.array([line.split() for line in field.strip().split("\n")],dtype=int)\
                                     for field in file.read().split("\n\n")]
    
lines  = lambda field: [list(line) for line in field] \
                      +[list(line) for line in field.transpose()] #\
                      #+[list(field.diagonal()), list(np.fliplr(field).diagonal())]
   
bingo = False
first_bingo = True    

for number in called_numbers:
    removelist = []
    for nr,field in enumerate(fields):
        if number in field:
            fields[nr] = np.where(field==number, -1, field)
            bingo = ([-1,-1,-1,-1,-1] in lines(fields[nr]))
            if bingo:
                if first_bingo or len(fields) == 1:
                    print("BINGO - we have the {} winner!".format({True:"first",
                                                                   False:"last"}[first_bingo]))
                    bingofeld = np.where(fields[nr]==-1, 0, field)
                    board_score = sum(set(bingofeld.flatten())) * number
                    print("Part{} solution-score: {}".format({True:1,
                                                              False:2}[first_bingo],
                                                             board_score))
                    first_bingo = False
                removelist.append(nr)
                bingo = False
    if len(removelist)>0:
        if len(fields) == 1:
            break
        for discard_no in sorted(removelist,reverse=True):
            fields.pop(discard_no)
        removelist = []
