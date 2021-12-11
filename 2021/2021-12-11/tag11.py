with open("t11input","r") as file:
     map_dict = {row + col*1j:int(value_str) for row,line in enumerate(file.readlines()) 
                                             for col,value_str in enumerate(line.strip())}

def increase_value(coords, map_file,flash_counter):
    map_file[coords] +=1
    if map_file[coords] == 10:
        flash_counter += 1
        for diff in [(x+y) for x in [-1,0,1] for y in [-1j,0,1j]]:
            if diff+coords in map_file:
                map_file,flash_counter = increase_value(coords+diff, map_file,flash_counter)
    return map_file, flash_counter           

flash_counter = 0
step_counter = 0
while not sum(map_dict.values()) == 0:
    step_counter += 1
    for coords in map_dict.keys():
        map_dict,flash_counter = increase_value(coords,map_dict, flash_counter)
    map_dict = {k:v if v <10 else 0 for k, v in map_dict.items()}
    if step_counter == 100:
        print("Part1, solution: ", flash_counter)
print("Part2, sync flashing ", step_counter)
        