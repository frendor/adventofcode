#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("puzzle","r") as infile:
    data = [row.strip().split() for row in infile.readlines()]

#Part1:
#   Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# A - Rock; B - Paper; C - Scissors 
# X - Rock; Y - Paper; Z - Scissors

zyclic = "0120"
#azyclic = "2102"

enemy_choice = lambda c1: 'ABC'.index(c1)
my_choice = lambda c2: 'XYZ'.index(c2)
win_loss_score = lambda ec,mc: 6 if zyclic[zyclic.index(str(enemy_choice(ec))) + 1] == str(my_choice(mc)) else\
                       3 if enemy_choice(ec) == my_choice(mc) else\
                       0 

score = sum([win_loss_score(c1,c2) +( "XYZ".index(c2)+1) for c1,c2 in data])
print(f"Part1: {score}")

#part2
# X - lose; Y - draw; Z - win
win_loss_selector = lambda c1, o1: [mc for mc in "XYZ" if my_choice(o1)*3 == win_loss_score(c1,mc)][0]

print("Part2:",sum([win_loss_score(c1,win_loss_selector(c1,o1)) + "XYZ".index(win_loss_selector(c1,o1))+1 for c1,o1 in data]))


