import numpy as np

with open("t5input","r") as file:
    vent_lines = [[complex(*map(int,values.split(","))) for values in line.strip().split(" -> ") ]  for line in file.readlines() ]
