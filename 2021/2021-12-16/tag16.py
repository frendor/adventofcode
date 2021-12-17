from numpy import prod
with open("t16example") as file:
    examples = file.read().split("\n")

with open("t16examples2") as file:
    examples2 = file.read().split("\n")


with open("t16input") as file:
    puzzle = file.readline().strip()


hex_to_bin = lambda zahl: "".join([bin(int(f"0x{digit}",16))[2:].zfill(4) for digit in zahl])
gt = lambda value: 1*(value[0]>value[1])
lt = lambda value: 1*(value[0]<value[1])
eq = lambda value: 1*(value[0] == value[1])

type_dict = {0: sum,
             1: prod,
             2: min,
             3: max,
             5: gt,
             6: lt,
             7: eq,
             }


def get_value(content):
    version = int(content[:3],2)
    version_sum = version 
    remaining_content = content[6:]
    bin_value = ''
    while remaining_content[0] == '1':
        _, *partnumber = remaining_content[:5]
        bin_value += "".join(partnumber)
        remaining_content = remaining_content[5:]
    _, *partnumber = remaining_content[:5]
    bin_value += "".join(partnumber)
    remaining_content = remaining_content[5:]
    result = int(bin_value,2)

    return remaining_content, version_sum, result

    
def analyse_operator_type0(content):

    version = int(content[:3],2)
    version_sum = version 
    type_id = int(content[3:6],2)
    payload_length = int(content[7:7+15],2)
    payload = content[7+15:7+15+payload_length]

    rest = content[7+15+payload_length:]
    values = []
    while payload and int(payload,2)>0:
        payload,version, val = analyse_packet(payload)
        version_sum += version
        values.append(val)

    result = type_dict[type_id](values)
    return rest, version_sum, result 
    
def analyse_operator_type1(content):
    version = int(content[:3],2)
    version_sum = version 
    type_id = int(content[3:6],2)
    number_of_subblocks = int(content[7:7+11],2)
    
    rest = content[7+11:]
    values = []
    for subblock_nr in range(number_of_subblocks):
            rest, version, val = analyse_packet(rest)
            values.append(val)
            version_sum += version
    result = type_dict[type_id](values)
    return rest, version_sum , result
    

def analyse_packet(packet):
    if int(packet[3:6],2) == 4:
        rest, version_sum, result = get_value(packet)
    elif packet[6]== '1':        
        rest, version_sum, result = analyse_operator_type1(packet)
    else: 
        rest, version_sum, result = analyse_operator_type0(packet)        
    return rest, version_sum , result    

def analyse_signal(message):
    signal = hex_to_bin(message)
    rest, version_counter, result = analyse_packet(signal)
    print("".center(30,"="))
    print(f"Part1 Sum of versionnumbers: {version_counter}")
    print(f"Part2 Solution:", result)
    print("".center(30,"="))

#for message in examples2:
#    analyse_signal(message)
#analyse_signal("38006F45291200")
analyse_signal(puzzle)