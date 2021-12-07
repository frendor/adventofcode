import numpy as np
import timeit

with open("t6example","r") as file:
    example_states = list(map(int, file.read().split(",")))

with open("t6input","r") as file:
    puzzle_states = list(map(int, file.read().split(",")))

#part1 #brute force
def count_fishes_bf(initial_state, max_day,silent = False):
    fish_states = np.array(initial_state)
    day = 1 
    while day <= max_day:
        fish_rep = (0 == fish_states)
        fish_mod = -1*(0 < fish_states) 
        fish_states += fish_mod
        fish_states += 6*fish_rep
        fish_states = np.append(fish_states, 8*np.ones(fish_rep.sum()))
        day += 1
    if not silent:         
        print(f"Brute Force: Day {day-1}: Number of fishes (solution): ", fish_states.shape[0])

#recursive approach, still takes time...
def new_fish(day_nr,max_day = 256):
    if day_nr >= max_day: 
        return 0
    else:
        fish_count = 1 
        times_left = int((max_day - day_nr-9)/7)+1
        mature_count = sum([new_fish(day_nr + 9 + 7 * step, max_day) for step in range(times_left)]) 
        return fish_count + mature_count


def count_fishes(fish_states, max_day, silent = False):   
    fish_dict = {age:fish_states.count(age) for age in set(fish_states)}
    fish_count = 0
    for age,age_count in fish_dict.items():
        fish_count +=  age_count * new_fish(age-9, max_day)
    if not silent:    
        print(f"Recursive: Tag: {max_day} Anzahl der Fische: {fish_count}")

#better one:

def count_fishes2(initial_state, max_day, silent = False):
    new_fish_dict = {day:0 for day in range(1,max_day+1)}
    initial_dict = {age-8:initial_state.count(age) for age in set(initial_state)}
    new_fish_dict.update(initial_dict)

    for day in sorted(new_fish_dict.keys()):
        fishes = new_fish_dict[day]
        for next_fish_day in [day+9+7*step for step in range(int((max_day - day-9)/7)+1)]:
            if next_fish_day <= max_day: 
                new_fish_dict[next_fish_day] += fishes
    if not silent:
        print(f"Dict-counter: Tag: {day} Anzahl aller Fische: ", sum(new_fish_dict.values()))

#Part1:
count_fishes_bf(example_states, 80)
count_fishes(puzzle_states, 80)
#Part2:
count_fishes2(puzzle_states, 256)
print()
print("Brute force with 80 Days:  ".ljust(30)\
        +"{0:.4f} ms".format(1000 *timeit.timeit('count_fishes_bf(puzzle_states,80,True)', setup="from __main__ import count_fishes_bf, puzzle_states",number = 50)))
print("Recursive with 80 Days:  ".ljust(30)\
        +"{0:.4f} ms".format(1000 *timeit.timeit('count_fishes(puzzle_states,80,True)', setup="from __main__ import count_fishes, puzzle_states",number = 50)))
print("Dict-counting with  80 Days:  ".ljust(30) \
      +"{0:.4f} ms".format(1000 *timeit.timeit('count_fishes2(puzzle_states,80,True)', setup="from __main__ import count_fishes2, puzzle_states",number = 50)))
print("Dict-counting with 256 Days:  ".ljust(30),end="")

print("{0:.4f} ms".format(1000 * timeit.timeit('count_fishes2(puzzle_states,256,True)', setup="from __main__ import count_fishes2, puzzle_states",number = 50)))