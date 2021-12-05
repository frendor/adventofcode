import numpy as np

with open("t5input","r") as file:
    vent_lines = [[complex(*map(int,values.split(","))) for values in line.strip().split(" -> ") ]  for line in file.readlines() ]

def count_dangerouspoints(part2=True):
    vent_coords = []
    for startpoint,endpoint in vent_lines:
        if (startpoint.real == endpoint.real) or (startpoint.imag == endpoint.imag):
            #print(f"Eine gerade Linie gefunden zwischen {startpoint} und {endpoint}")
            if startpoint.real == endpoint.real:
                all_steps = np.linspace(startpoint.imag, endpoint.imag, abs(int(startpoint.imag-endpoint.imag))+1)
                vent_coords += [complex(startpoint.real,step) for step in all_steps]
            elif startpoint.imag == endpoint.imag:
                all_steps = np.linspace(startpoint.real, endpoint.real, abs(int(startpoint.real-endpoint.real))+1)
                vent_coords += [complex(step,startpoint.imag) for step in all_steps]
        elif abs(startpoint.imag - endpoint.imag) == abs(startpoint.real - endpoint.real) and part2:
            #print(f"Eine diagonale Linie gefunden zwischen {startpoint} und {endpoint}")
            x_step = np.linspace(startpoint.real, endpoint.real, abs(int(startpoint.real-endpoint.real))+1)
            y_step = np.linspace(startpoint.imag, endpoint.imag, abs(int(startpoint.real-endpoint.real))+1)
            new_coords = [complex(x_step, y_step[nr]) for nr,x_step in enumerate(x_step) ]
            #print(new_coords)
            vent_coords += new_coords

    vent_dict = {}  
    for coords in vent_coords:
        vent_dict.setdefault(coords,0)
        vent_dict[coords] += 1 
    part_str = {True:2, False:1}[part2]

    print(f"Part{part_str}: Dangerous Points found: ",sum([1 for value in vent_dict.values() if value > 1]))

count_dangerouspoints(part2 = False)
count_dangerouspoints(part2 = True)
