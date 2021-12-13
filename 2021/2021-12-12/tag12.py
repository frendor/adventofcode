from itertools import chain

with open("t12input","r") as file:
    all_connections = [line.strip().split("-") for line in file.readlines()]
    
all_caves = set(chain(*all_connections))
con_dict = {cave:set(chain(*[[other_cave for other_cave in con if other_cave != cave] for con in all_connections if cave in con])).difference(cave) for cave in all_caves}

visit_twice = lambda path: max([path.count(cave) if cave.islower() and cave not in ["start","end"] else 0 for cave in set(path) ])==2

def step(cave,path,part2):
    if cave == "end":
        return [path]

    path_list = []
    for connection in con_dict[cave]:
        if (connection not in path) \
         or connection.isupper() \
         or (part2 and not visit_twice(path) and connection != "start") :
            next_path = path + [connection]
            path_list.extend(step(connection,next_path,part2))

    return path_list

print("Part1: Anzahl gefundener Pfade: ", len(step("start",["start"],part2=False)))    
print("Part2: Anzahl gefundener Pfade: ", len(step("start",["start"],part2=True)))    
