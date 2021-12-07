import numpy as np

with open("t7input","r") as file:
    input_states = np.array(file.read().split(","),dtype=int)


differences = [sum(abs(input_states - end_pos)) for end_pos in range(input_states.min(), input_states.max()+1)]
print(f"Part1: {differences.index(min(differences))} Fuel spend: {min(differences)}")   

new_dist = lambda dist: sum(range(abs(dist)+1))

part2_differences = [sum(map(new_dist, input_states - end_pos)) for end_pos in range(input_states.min(), input_states.max()+1)]
print(f"Part2: {part2_differences.index(min(part2_differences))} Fuel spend: {min(part2_differences)}")   
