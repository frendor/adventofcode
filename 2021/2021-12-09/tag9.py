with open("t9input","r") as file:
     cave_map = {row + col*1j:int(value_str) for row,line in enumerate(file.readlines()) 
                                             for col,value_str in enumerate(line.strip())}

find_minimum = lambda coords, map_dict: map_dict[coords] < min([map_dict[coords + diff] for diff in [1,-1,1j,-1j] if coords + diff in map_dict])
find_good_neighbor = lambda coords, map_dict: set(coords + diff for diff in [1,-1,1j, -1j] if (coords+diff in map_dict) and (map_dict[coords+diff] < 9) )

#Part1 
print("Part1: Solution: ", sum([1+value for coords, value in cave_map.items() if find_minimum(coords, cave_map)]))


def explore_basin(coords, map_dict, known_coords):
    known_coords.add(coords)
    neighbors = find_good_neighbor(coords,map_dict)

    for new_coord in neighbors:
        if new_coord not in known_coords:
            known_coords = explore_basin(new_coord, map_dict, known_coords)
    return known_coords

open_coords = set(coords for coords,value in cave_map.items() if value<9)
basins = []

while len(open_coords):           
    basin = explore_basin(open_coords.pop(), cave_map, set())
    basins.append(len(basin))
    open_coords -= basin

result = 1
for number in sorted(basins,reverse=True)[:3]:
    result *= number
print("Part2: Solution: ", result)
    