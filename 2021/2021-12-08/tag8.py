
with open("t8example","r") as file:
    example_list = [[digits.split() for digits in line.split("-")] for line in file.read().strip().replace(" |\n","-").split("\n")]

with open("t8input","r") as file:
    signal_list = [[digits.split() for digits in line.split(" | ")] for line in file.read().strip().split("\n")]

print("Part1 Solution: " , sum([(len(digit) in [2,3,4,7]) for line in signal_list for digit in line[-1]]))

def part2_decode_pattern(all_number_list, value_codes):
    all_numbers = set(all_number_list)
    len_dict= {2:1,
               3:7,
               4:4,
               7:8}
    code_dict = {len_dict[len(number)]:set(number) for number in all_numbers if len(number) in len_dict.keys()}
    bar_of_four = code_dict[4] - code_dict[1]
    for number in all_numbers:
        if number in code_dict.values():
            continue
        if len(number)==5:
            if code_dict[7].issubset(number):
                code_dict[3] = set(number)
            elif bar_of_four.issubset(number):
                code_dict[5] = set(number)
            else:
                code_dict[2] = set(number)
        if len(number) == 6:
            if not code_dict[1].issubset(number):
                code_dict[6] = set(number)
            elif not bar_of_four.issubset(number):
                code_dict[0] = set(number)
            else:
                code_dict[9] = set(number)

    output_value = "".join([str(k) for digit in value_codes for k,v in code_dict.items() if set(digit) == v])
    return int(output_value)

print("Part2 Solution: ",sum([part2_decode_pattern(*line) for line in signal_list]))
    