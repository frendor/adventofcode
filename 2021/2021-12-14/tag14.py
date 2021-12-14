from itertools import chain

with open("t14input","r") as file:
    template, rules = file.read().split("\n\n")

rule_dict = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in rules.split("\n")}

def growth_step(template):
    next_step = ""
    for nr,char in enumerate(template[:-1]):
        pair = f"{char}{template[nr+1]}"
        if pair in rule_dict.keys(): 
            next_step+=f"{char}{rule_dict[pair]}"
        else: 
            next_step+=char
    next_step += template[-1]
    return next_step

#part1 - brute force
step_counter = 1
polymer = template
while step_counter <= 10:
    polymer = growth_step(polymer)
    step_counter += 1

element_counter = {}
for char in polymer:
    element_counter.setdefault(char,0)
    element_counter[char]+=1
print("Part1 Solution: ", max(element_counter.values()) - min(element_counter.values()) )
    
#part2
def growth_step2(pair_dict,element_counter):
    new_pair_dict = {k:0 for k,v in pair_dict.items()}
    for pair, value in pair_dict.items():        
        element_counter[rule_dict[pair]] += value
        for new_pair in rule_pair_dict[pair]:
            new_pair_dict[new_pair] += value
    return new_pair_dict, element_counter

elements = set(rules.replace("\n","").replace(" -> ",""))
element_counter = {}
for char in elements:
    element_counter.setdefault(char,0)
    
rule_pair_dict = {k:[k[0]+v,v+k[1]] for k,v in rule_dict.items()}
pair_dict = {pair:0 for pair in rule_pair_dict.keys()}

for nr,char in enumerate(template[:-1]):
    pair = f"{char}{template[nr+1]}"
    pair_dict.setdefault(pair,0)
    pair_dict[pair] += 1
    element_counter[char] += 1
element_counter[template[-1]] += 1

step_counter = 1
while step_counter <= 40:
    pair_dict, element_counter = growth_step2(pair_dict,element_counter)
    if step_counter in [10,40]:
        print(f"Part2 Step {step_counter:2d} Solution: ", max(element_counter.values()) - min(element_counter.values()) )
    step_counter += 1


