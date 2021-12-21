from math import floor, ceil
from functools import reduce
from itertools import permutations
from copy import copy, deepcopy

def slice_int(some_string):
    if not some_string[0].isnumeric():
        return False
    for nr,char in enumerate(some_string):
            if char.isnumeric():
                continue
            else:
                break
    return int(some_string[:nr]), some_string[nr:]

def read_number(number_string, depth=0):
    rest = number_string[1:]
    if rest[0] == "[":
        l , rest = read_number(rest,depth+1)
    else:
        l, rest = slice_int(rest)
        rest = rest[1:]
    if rest[0] == "[":
        r , rest = read_number(rest,depth+1)
    else:
        r , rest = slice_int(rest)
        rest = rest[1:]
    if rest:
        return [l,r], rest[1:]
    else: 
        return [l,r]  

def reduce_number(number,show_number=False):
    if show_number:
        print('Starte: ',number, end=" --> ")
    has_changed = is_completly_checked = False
    while not is_completly_checked:
        for check in [check_explode,check_split]:
            number, has_changed =  check(number)

            if has_changed:
                break
        else:
            is_completly_checked = True
    if show_number:
        print(number)
    return number
                

def check_explode(number, depth=1, from_left=0, from_right = 0, has_changed = False):

    to_left = to_right = 0
    l_to_r = r_to_l = 0
    run_once = True
        
    while run_once or r_to_l or l_to_r:
        run_once = False
        for part_nr, side in enumerate(number):

            if isinstance(side,list):
                if part_nr == 0:
                    to_left, number[part_nr], l_to_r, has_changed = check_explode(side, depth + 1, from_left=from_left, from_right=r_to_l, has_changed=has_changed)
                    from_left = r_to_l = 0  

                else:
                    r_to_l, number[part_nr], to_right, has_changed = check_explode(side, depth + 1, from_left=l_to_r, from_right=from_right, has_changed = has_changed)
                    from_right = l_to_r = 0
                
                has_changed = any([to_left, l_to_r, to_right, r_to_l, has_changed])
                    
                if depth>3 and not has_changed:
                    if part_nr == 0:
                        to_left, l_to_r = side
                    elif part_nr == 1:
                        r_to_l, to_right = side
                    number[part_nr] = 0
                    has_changed = True
 
                                
            elif part_nr == 0 and (from_left or r_to_l):
                number[part_nr] += from_left + r_to_l
                r_to_l = from_left = 0
            elif part_nr == 1 and (from_right or l_to_r):
                number[part_nr] += from_right + l_to_r
                from_right = l_to_r = 0        
    if depth == 1:
        return number, has_changed
    else:
        return to_left, number, to_right, has_changed

    
def check_split(number):    
    for nr,part in enumerate(number):
        if isinstance(part,list) :
            number[nr], has_changed = check_split(part)
            if has_changed:
                return number, has_changed
            
        elif part > 9:
            number[nr] = [floor(part/2), ceil(part/2)]
            #print("Spalte ", number)
            return number, True

    return number, False

def calculate_magnitude(number):
    for side_nr,factor in enumerate([3,2]):
        if isinstance(number[side_nr],list):
            number[side_nr] = calculate_magnitude(number[side_nr])
        number[side_nr] *= factor
    return sum(number)

#add_numbers = lambda n1,n2: reduce_number([reduce_number(n1),reduce_number(n2)])

def add_numbers(n1,n2):
    l = deepcopy(n1)
    r = deepcopy(n2)
    return reduce_number([reduce_number(l),reduce_number(r)])
    

add_numberlist = lambda numberlist: reduce(add_numbers,numberlist)


with open("t18example3") as file:
    numbers3 = [read_number(line.strip()) for line in file.readlines()]


with open("t18input") as file:
    puzzle = [read_number(line.strip()) for line in file.readlines()]

p1_puzzle = deepcopy(puzzle)
#part1
print(f"Part1: Magnitude: {calculate_magnitude(add_numberlist(p1_puzzle))}")
# part2

print("Part2: Hightest possible Magnitude: ", max([calculate_magnitude(add_numberlist(pair)) for pair in permutations(puzzle, 2)]))
