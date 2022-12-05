
with open("puzzle","r") as infile:
    data = infile.read()
    
drawing, schedule = data.split("\n\n")

stack_amount =  max([int(val) for val in drawing.split("\n")[-1] if val.isnumeric()])

moves = [(int(line.split()[1] ),int(line.split()[3]),int(line.split()[5])) for line in schedule.split("\n") if "move" in line]

### Part1
def part1():
    crate_dict = {stack_nr+1:[line[1 + stack_nr*4] for line in drawing.split("\n")[:-1] if line[1 + stack_nr*4].isupper()] for stack_nr in range(stack_amount) }       

    for am, f, t in moves:
        for step in range(am):
            c = crate_dict[f].pop(0)
            crate_dict[t] = [c] + crate_dict[t]

    print("Part1: ","".join([v[0] for v in crate_dict.values()]))

### Part2
def part2():
    crate_dict = {stack_nr+1:[line[1 + stack_nr*4] for line in drawing.split("\n")[:-1] if line[1 + stack_nr*4].isupper()] for stack_nr in range(stack_amount) }       

    for am, f, t in moves:
        c = crate_dict[f][:am]
        crate_dict[f] = crate_dict[f][am:] 
        crate_dict[t] = c + crate_dict[t]
        
    print("Part2: ","".join([v[0] for v in crate_dict.values()]))

part1()
part2()