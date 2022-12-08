#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:18:58 2022

@author: frendor
"""

with open("puzzle","r") as infile:
    data = [line.strip() for line in infile.readlines()]
    


pfad = lambda ad: "/" + "/".join(ad) + "/" if ad else "/"

def change_dir(ad, command):
    if command.startswith("$ cd"):
        param = command.split()[2]
        if param == "/":
            ad = []
        elif param == "..":
            ad.pop()
        else:
            ad.append(param)
    return ad

ad = []
filesystem = {}

while data:
    line = data.pop(0)
    
    if line.startswith("$ cd"):
        ad = change_dir(ad,line)
    elif line.startswith("$ ls"):
        for nr,nl in enumerate(data):
            if nl[0] == "$":
                break
        file_list = [ pfad(ad+[entry.replace("dir ","")]) if entry.startswith("dir") else entry for entry in data[:nr] ]
        data = data[nr:]
        filesystem[pfad(ad)] = file_list
    else:
        filesystem[pfad(ad)].append(line)

def dir_walk(directory):
    size = 0
    for entry in filesystem[directory]:
        if entry.startswith("/"):
            size += dir_walk(entry)
        else:
            size += int(entry.split()[0])
    return size
            
### Part1:
print("Part1: ",sum([dir_walk(directory) for directory in filesystem.keys() if dir_walk(directory)<=100000]))
  
### Part2:  
used_space = dir_walk("/")
free_space = 70000000 - used_space
required_space = 30000000 - free_space

print("Part2: ", sorted([(dir_walk(directory),directory) for directory in filesystem.keys() if dir_walk(directory)>=required_space])[0])