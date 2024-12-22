#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:51:53 2024

@author: frendor
"""

with open("puzzle","r") as infile:
    raw_data= infile.read()

ordering_raw, updates_raw = raw_data.split("\n\n") 
ordering = {}
for line in ordering_raw.split("\n"):
    p,k = map(int,line.split("|"))
    ordering.setdefault(p,set())
    ordering[p].add(k)
            
updates = [[int(page) for page in line.split(",")] for line in updates_raw.split("\n") ]


def check_rules(rules, page, seq, sign):
    test_pages = set(seq)
    for nr in test_pages:
        if sign=="+":
            be,af = page, nr
        else:
            be,af = nr, page
        if be in rules and af in rules[be]:
            continue
        elif af in rules and be in rules[af]:
                return False
    return True
            
def switch_pages(page1, page2, rules):
    if page1 in rules and page2 in rules[page1]:
        return False
    elif page2 in rules and page1 in rules[page2]:
        return True
    else:
        return False
     

def sort_sequence(seq,rules):
    new_seq = seq[:1]
    for next_page in seq[1:]:
        for index,page in enumerate(new_seq):
            switch = switch_pages(page,next_page,rules)
            if switch == True:
                new_seq.insert(index,next_page)
                break
        if next_page not in new_seq:
            new_seq.append(next_page)
    if test_update(new_seq,rules):
        return new_seq
                
def test_update(seq,rules):
    is_ok = True
    for run,index in enumerate(range(len(seq))):
        page = seq[index]
        before_list,after_list = seq[:index], seq[index+1:]
        t1 = check_rules(rules, page, before_list, sign="-")
        if t1:
            t2 = check_rules(rules, page, after_list, sign="+")
        if t1 and t2:
            pass
        else:
            is_ok = False
    return is_ok

if __name__ =="__main__":
    result = 0
    corrected_results = 0
    for run,seq in enumerate(updates):
        if test_update(seq, ordering):
            #print(f"Sequence {run+1} ist ok")
            result += seq[int(len(seq)/2)]
        else:
            cor_seq = sort_sequence(seq,ordering)
            #print(f"Sequence {run+1} is not ok, correcting..ok")
            corrected_results += cor_seq[int(len(cor_seq)/2)]
    print("Teil1 ", result)
    print(f"Teil2: {corrected_results}")