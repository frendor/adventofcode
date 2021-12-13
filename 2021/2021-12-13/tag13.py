import numpy as np 

with open("t13input","r") as file:
    data,instructions = file.read().strip().split("\n\n")

coords = np.array([list(map(int,line.split(","))) for line in data.split("\n")])
#correction: The paper-width is 2*fold + 1. A equal-numbered papersize due to missing points in the last row results in non-sense. 
field = np.zeros(coords.max(axis=0)+[1,1] + ((coords.max(axis=0)) % 2==1) ).transpose()

show_field = lambda field: "\n".join(["".join(["{0:.0f}".format(nr) if nr else " " for nr in line]) for line in field])

for y,x in coords:
    field[x,y] = True

fold_list = [line[10:].strip().split("=") for line in instructions.split("\n")]

for nr,[axis_char, value] in enumerate(fold_list):

    x_val, y_val, splitfkt, flipfkt = {"x":[1,0,np.hsplit,np.fliplr],
            "y":[0,1,np.vsplit, np.flipud]}[axis_char]

    field = np.delete(field,int(value),axis=x_val)
    split1,split2 =  splitfkt(field,2)
    field = np.minimum(1,split1 + flipfkt(split2))
    if nr==0:
        print(f"Part1 Numbers of dots after 1 fold: {field.sum():.0f}" )
        
print("Result:\n"+show_field(field))
