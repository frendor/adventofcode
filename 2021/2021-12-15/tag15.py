from math import inf
from dataclasses import dataclass,field
from typing import Any
from queue import PriorityQueue


with open("t15example","r") as file:
    testmap = {(row + 1j*col):int(value) for row,line in enumerate(file.readlines()) for col,value in enumerate(line.strip())}

with open("t15input","r") as file:
    puzzlemap = {(row + 1j*col):int(value) for row,line in enumerate(file.readlines()) for col,value in enumerate(line.strip())}
#print(cavemap)

cavemap = testmap

end_point = complex(*max([[value.real, value.imag] for value in cavemap]))
avg_risk = sum(cavemap.values())/len(cavemap.values())*(end_point.imag+end_point.real)
waypoint_dict = {}

diff = [1,1j,-1,-1j]

show_row = lambda linenr, waypoints,map_dict: "".join([str(val) if (pos.real==linenr and pos in waypoints) else " " if pos.real==linenr else "" for pos,val in map_dict.items()  ])
show_map = lambda best_way,map_dict: "\n".join([show_row(row,best_way,map_dict) for row in range(1+int(max([pos.imag for pos in map_dict.keys()])))])
get_risklvl = lambda waypoints: sum([cavemap[position] for position in waypoints])

def next_step(position, waypoints, best_risklvl=avg_risk):
    current_risk_level = get_risklvl(waypoints)
    if position == end_point:
        return current_risk_level,waypoints
    if current_risk_level >= best_risklvl:
        return False,waypoints
    better_way = False
    for step in diff:
        new_pos = position + step            
        if new_pos in cavemap and not new_pos in waypoints:
            new_risklvl, current_way = next_step(new_pos, waypoints+[new_pos], best_risklvl)
                        
            if new_risklvl and new_risklvl <best_risklvl:
                waypoint_dict[new_pos] = current_way[current_way.index(new_pos):]
                #print(f"besseren Weg gefunden: Risk: {get_risklvl(current_way)}, Size: {len(current_way)}, Position: {current_way.index(new_pos)}")
                best_risklvl = new_risklvl
                better_way = current_way
            
    return best_risklvl, better_way

#first idea: some recursive approach, suitable for the example
best_risk, best_way = next_step(0,[])
print(f"Part1 Example: Solution {best_risk}")
print(show_map(best_way+[0],testmap))

@dataclass(order=True)
class Item:
    key: int
    position: Any=field(compare=False)

def my_dijkstra_pathfinder(cavemap):
    queue = PriorityQueue()
    open_notes = set(cavemap.keys())
    risk_dict = {0:(0,[])}
    end_point = complex(*max([[value.real, value.imag] for value in cavemap]))
    queue.put(Item(0,0))

    while not queue.empty():
        item = queue.get()
        actual_risk = item.key
        position = item.position
        waypoints = risk_dict[position][1]
        open_notes.remove(position)
        if not actual_risk == risk_dict[position][0]:
            actual_risk, waypoints = risk_dict[position][0]
            
            print("Hier hat es nicht gestimmt")
            
        for neighbor in [direction+position for direction in diff if direction+position in open_notes]:
            risk_dict.setdefault(neighbor,(inf,[]))
            
            if actual_risk + cavemap[neighbor] < risk_dict[neighbor][0]:
                risk_dict[neighbor] = (actual_risk + cavemap[neighbor], waypoints+[neighbor])
                
                queue.put(Item(actual_risk + cavemap[neighbor],neighbor))
        
    return risk_dict[end_point]
        

#part1: 
best_risk,best_path = my_dijkstra_pathfinder(puzzlemap)
print(f"Part1: Solution {best_risk}")
#print(show_map(best_path, puzzlemap))

#part2: "yes, i really want a PriorityQueue"
#repeat map:
end_point = complex(*max([[value.real, value.imag] for value in puzzlemap]))
hugh_map = {(end_point.real+1)*row + 1j*col*(end_point.imag+1) + coord:(val + row + col)%10+int((val + row + col)/10)  for row in range(5) for col in range(5) for coord, val in puzzlemap.items()}
hugh_risk,hugh_path = my_dijkstra_pathfinder(hugh_map)
print(f"Part2: Solution {hugh_risk}")
with open("hugh_map.txt","w") as outfile:
    outfile.write(show_map(hugh_path+[0], hugh_map))
