with open("t10input","r") as file:
     chunk_lines = file.readlines()

def line_tester(line):
    opener_list = []
    pair_dict = {")":"(",
                "]":"[",
                ">":"<",
                "}":"{"}
    part1_points = {")":3,
                "]":57,
                "}":1197,
                ">":25137}
    for char in line.strip():
        if char in pair_dict.values():
            opener_list.append(char)
        elif char in pair_dict.keys():
            if opener_list[-1] == pair_dict[char]:
                opener_list.pop(-1)
            else: 
                return part1_points[char],False

    closing_dict = {v:k for k,v in pair_dict.items()}
    opener_list.reverse()
    repair_list = [closing_dict[char] for char in opener_list]
    
    part2_points = {")":1,
                "]":2,
                "}":3,
                ">":4}
    line_score = 0
    for char in repair_list:
        line_score *= 5
        line_score += part2_points[char]
    return line_score, True

print("Part1: Checker Score: ",sum([line_tester(line)[0] for line in chunk_lines if not line_tester(line)[1] ]))
score_line = sorted([line_tester(line)[0] for line in chunk_lines if line_tester(line)[1]])
print("Part2: Autocomplete Score:", score_line[int(len(score_line)/2)] )
    