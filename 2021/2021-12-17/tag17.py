import numpy as np

with open("t17puzzle") as file:
    target = file.read()

target_dict = {coord: list(map(int,area.split(".."))) for coord, area in \
               [line.split("=")        for line in target[13:].split(", ") \
                                       if target[:13] == "target area: " ]}

start = 0j

flight_step = lambda position, velocity: position+velocity
v_diff = lambda velocity: velocity + 1-1j if velocity.real<0 else velocity - 1-1j if velocity.real > 0 else velocity - 1j
dist = lambda coords: sum([r**2 for r in coords])**0.5

max_distance =  dist([np.abs(coords).max() for coords in target_dict.values()])

def shoot():
    v0_range = [complex(x,y) for x in range(max(target_dict["x"])+1) for y in range(min(target_dict['y']),500) if dist([x,y]) <= max_distance]
    
    best_height = 0
    best_startspeed = 0
    getroffen = set()
    for v0 in v0_range:
        pos = 0
        step = 0
        velocity = v0
        current_best_height = 0
        
        while dist([pos.real, pos.imag]) < max_distance or pos.imag > start.imag:

            pos = flight_step(pos,velocity)
            velocity = v_diff(velocity) 
            if pos.imag > current_best_height:
                current_best_height = pos.imag
            step += 1
            if target_dict['x'][0]<= pos.real <= target_dict['x'][1] \
            and target_dict['y'][0]<= pos.imag <= target_dict['y'][1]:
                getroffen.add(v0)
                if current_best_height > best_height:
                    best_height = current_best_height
                    best_startspeed = v0
                break

    print(f"Part1: Best height {int(best_height)} with {best_startspeed}")
    print(f"Part2: So viele führen zum Ziel: {len(getroffen)}")
    return getroffen
    
shoot()       