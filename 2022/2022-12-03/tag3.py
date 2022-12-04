#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from string import ascii_letters

with open("puzzle") as content_list_file:
    content_list = [rucksack.strip() for rucksack in content_list_file.readlines() if rucksack]

get_common_items = lambda rucksack: set(rucksack[:len(rucksack)//2]).intersection(set(rucksack[len(rucksack)//2:]))
get_score = lambda item: ascii_letters.index(item) + 1

priority_score = sum([get_score(item) for rucksack in content_list for common_items in get_common_items(rucksack) for item in common_items])

print(f"Part1: {priority_score}")

badge_priority_score = sum([get_score(badge) for nr in range(len(content_list)//3) for r1,r2,r3 in (content_list[3*nr:3*nr+3],) for badge in set(r1).intersection(set(r2)).intersection(set(r3)) ])


print(f"part2: {badge_priority_score}")