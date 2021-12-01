#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:53:50 2020

@author: frendor
"""
from itertools import product

import re

DAY = 19

PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"

def load_input(filename = EXAMPLE ):
    with open(filename,"r") as file:
        allrules, messages =  file.read().split("\n\n")
        rules = {int(rule_nr):rule.strip() for rule_nr, rule in [tuple(line.strip().split(":")) for line in allrules.split("\n") ]}
        message_list = [line.strip() for line in messages.strip().split("\n")]
    return rules, message_list

rule_parser = lambda match,rule_dict: "".join([read_rule(rule_dict,int(some_rule)) for some_rule in match['new_rules'].split()])
#rule_join = lambda match: "("+"|".join(["".join(combi) for combi in product(*re.findall(r"\(([a-z]+)\|([a-z]+)\)",match[0])) if all(combi)])+")"

def rule_join(match):
    match_list = set(re.findall("\w+",match[0]))
    joined_match = "("+"|".join(match_list)+")"
    #print(f"bilde Vereinigung: {match[0]} ->  {joined_match}")
    
    return joined_match

def rule_product(match):
    print("bilde Produkt: ",match[0], end=" -> ")
    factor_list = re.findall(r"(?P<p1>\w+)(?=\()"\
                            +"|((?<=[\(])[a-z|]+(?=[\|\)}]))"\
                            +"|(?<=\))(?P<p3>\w+)",match[0])
    factor_list = [factor.split("|") for term in factor_list for factor in term if factor]
    comb_list = set(["".join(combination) for combination in product(*factor_list)      ])
    new_combination_list = "("+"|".join(comb_list)+")"
    #print(factor_list)
    #print(list(product(*factor_list)))
    print(new_combination_list)
    
    return new_combination_list
    

def read_rule(rule_dict,rule_nr):
    #print(f"Rule{rule_nr}: {rule_dict[rule_nr]}")
    rule = rule_dict[rule_nr]
    if re.search(r"\"(?P<char>[a-z]+)\"", rule):
        rule = re.search(r"\"(?P<char>[a-z]+)\"", rule)['char']
        #print(f"Rule{rule_nr}: {rule_dict[rule_nr]} -> {rule}")
        return rule
    rule = re.sub(r"(?P<new_rules>(\d+ )+\d+|\d+)",lambda res: rule_parser(res,rule_dict),rule)
    #print ("W1: ",rule)
    
    prev_line = ""
    while prev_line is not rule:
        prev_line = rule
        rule = re.sub(r"\((\w+\|\([a-z|]+\))\)"\
                      +"|\(?\([a-z|]+\)\|\([a-z|]+\)\)?"\
                      +"|\(?(\([a-z|]+\)\|\w+)\)?",rule_join,rule)
        #print("Z2",rule)
        for pnr,pattern in enumerate([" \| ".join(combination) for combination in product(["([a-z]+)","(\([a-z|]+\))"],repeat=2)]):
            #if re.search(pattern,rule):
            #    print(re.search(pattern,rule))
            rule = re.sub(pattern,r"(\1|\2)",rule)
            
            rule = re.sub( r"\(?(\w+\|?\([a-z|]+\))\)?"\
                          +"|\(?\([a-z|]+\)\([a-z|]+\)\)?"\
                          +"|\(?(\([a-z|]+\)\|?\w+)\)?",
                           rule_product, rule)
            #print("zusammenfassung: ",rule)
            #print(f"pat{pnr}: {pattern} ",rule)
        #        rule = re.sub(r"(\w+) \| (\w+)",r"(\1|\2)",rule)
        #        print("Z3",rule)
        #        rule = re.sub(r"\(([a-z|]+)\) \| (\w+)",r"(\1|\2)",rule)
        #        print("Z4",rule)
        #        rule = re.sub(r"\(([a-z|]+)\) \| \(([a-z|]+)\)",r"(\1|\2)",rule)
        #        print("Z5",rule)
    #print(f"Rule{rule_nr}: {rule_dict[rule_nr]} -> {rule}")    
    rule_dict[rule_nr] = rule
    return rule

def check_msg_list(msg_list,rules):
    pattern = read_rule(rules,0)
    rules = r_dict
    pattern = rules[0]
    good_msgs = []
    for msg in mlist:
        result = re.match(pattern,msg)
        print(result)
        if result and msg == result[0]:
            print("Gute Nachricht gefunden: ",msg)
            good_msgs.append(msg)
            
        #if result and len(result[0]) == len(msg):
        #else:
        #    #print("Schlechte Nachricht gefunden: ",msg)
    print(f"Part1: Good Messages found: {len(good_msgs)}") 
    return good_msgs

if __name__ == "__main__":
    r_dict, mlist = load_input()
    check_msg_list(mlist, r_dict)
    