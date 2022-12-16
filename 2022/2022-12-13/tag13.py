#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 12:25:07 2022

@author: frendor
"""

with open("puzzle","r") as infile:
    data = infile.read()


def parse_brakket(p):
    this_list = []
    if p[0] == "[" and p[-1]=="]":
        p_rest = p[1:]
        #print("Parse nun: ",p_rest)
        
        while p_rest is not "]":
            if p_rest[0].isnumeric():
                #print("Zahl gefunden: ",p_rest[0])
                for nr,char in enumerate(p_rest):
                    #print("bin nun hier: ",char," und das ist",char.isnumeric() )
                    if not char.isnumeric():
                        break
                #print("komplette Zahl: ",p_rest[:nr])
                this_list.append(int(p_rest[:nr]))
                p_rest = p_rest[nr:]
                #print("Rest: ",p_rest)
            if p_rest[0] == ",":
                p_rest=p_rest[1:]
                #print("Werfe komma weg:", p_rest)
            if p_rest[0] == "[":
                #print("Neue Klammer gefunden")
                klammer_counter = -1
                for knr,char in enumerate(p_rest):
                    if char == "[":
                        klammer_counter+=1
                    if char == "]":
                        if klammer_counter == 0:
                            break
                        else:
                            klammer_counter -=1
                            
                #print("Neue Klammer gefunden: ",p_rest[0:knr+1])
                nb = parse_brakket(p_rest[0:knr+1])
                this_list.append(nb)
                p_rest = p_rest[knr+1:]
            
    #print("Von ",p," gebe zurück: ",this_list)
    return this_list
    
def compare_2brakkets(left,right):
    
    len_result =  1*(len(left) < len(right)) + 2*(len(left) == len(right))
    
    for nr,(l,r) in enumerate(zip(left[:len(right)],right)):
        if isinstance(l,int) and isinstance(r,int):
            
            if l>r:
                
                return 0
            elif l<r:
                
                return 1
            else:
                res = 2
        elif isinstance(l,list) and isinstance(r,list):
            res = compare_2brakkets(l,r)
        else:
            if isinstance(l,list):
                res = compare_2brakkets(l,[r])
            else:
                res = compare_2brakkets([l],r)
        if res < 2:
            return res
    
    return len_result    
    
  
class Brakket(object):
    def __init__(self, package_str):
        self.package = parse_brakket(package_str)
        
    def __gt__(self, other_brakket):
        result = compare_2brakkets(self.package, other_brakket.package)
        return result > 0
        
    def __repr__(self):
        return f"{self.package}"
    def __eq__(self, other_brakket):
        return self.package == other_brakket.package
        
pair_list = [(parse_brakket(p1.strip()), parse_brakket(p2.strip())) for nr,package in enumerate(data.split("\n\n")) 
                                                                    for p1,p2 in (package.split("\n"),)]
#print(pair_list)
p1_result = [nr+1 for nr,(p1,p2) in enumerate(pair_list) if compare_2brakkets(p1,p2)]
print(f"Part1: {sum(p1_result)}")

##### Part2:

divider_packages = [Brakket('[[2]]'),Brakket('[[6]]')]

l1 = [Brakket(line) for line in data.split("\n") if line] + divider_packages
sorted_packages = sorted(l1,reverse=True)
p2_r1, p2_r2 = [nr+1 for nr, elem in enumerate(sorted_packages) if elem in divider_packages ]
print(f"Part2: decoder key = {p2_r1*p2_r2}")