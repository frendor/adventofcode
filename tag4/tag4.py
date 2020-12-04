#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:30:25 2020

@author: frendor
"""

import re

DAY = 4
DEBUG = False


PUZZLE_FILE = f"t{DAY}puzzle.input"
EXAMPLE_FILE = f"t{DAY}puzzle.example"


def load_input(filename = PUZZLE_FILE ):
    with open(filename,"r") as file:
        input_lines = file.readlines()
    return input_lines
    
def parse_passport_file(pass_input,debug=DEBUG):
    passport_list = []
    tmp_dict = {}
    for line in pass_input:
        if line is not "\n":
            itemlist = [elem.split(":") for elem in line.split()]
            for key, value in itemlist:
                if key in tmp_dict:
                    print(f"Warning: Doppelter Eintrag im Pass: {key}")
                tmp_dict[key] = value
        else:
            if debug: 
                print(f"Gefundener Satz: {tmp_dict}\n")
            passport_list.append(tmp_dict)
            tmp_dict = {}
    #Letzten Eintrag nicht vergessen:
    if debug: 
        print(f"Gefundener letzter Satz: {tmp_dict}\n")
    passport_list.append(tmp_dict)
    
    return passport_list     
        
def check_passport_simple(pass_dict,debug=DEBUG):
    '''byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        Optional: cid'''
    required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    optional_field = ['cid']
    
    pass_valid = False
    req_field_test = [(field in pass_dict) for field in required_fields]
    if not False in req_field_test:
        pass_valid = True
    opt_field_test = [(field in pass_dict) for field in optional_field]
    if not False in opt_field_test:
        if debug:
            print(f"Optionale Angaben vorhanden: {optional_field}")
    
    return pass_valid

def check_passport_with_validation(pass_dict,debug=DEBUG):
    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    
    '''
    pass_valid = [False for elem in range(7)]
    
    req_limits = {'byr':[1920,2002],
                  'iyr':[2010,2020],
                  'eyr':[2020,2030],}
    for nr,(key, [low,high]) in enumerate(req_limits.items()): 
           
            if low <= int(pass_dict[key]) <= high:
                pass_valid[nr] = True
    
    #hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.
    
    if pass_dict['hgt'][:-2].isnumeric() \
       and (pass_dict['hgt'][-2:] == "cm"\
            and 150 <= int(pass_dict['hgt'][:-2]) <= 193) \
         or \
           (pass_dict['hgt'][-2:] == "in"\
            and 59 <= int(pass_dict['hgt'][:-2]) <= 76):
        pass_valid[3] = True
    
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if re.search(r"#[0-9a-f]{6}",pass_dict['hcl']) and len(pass_dict['hcl'])==7:
        pass_valid[4] = True

    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if pass_dict['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
        pass_valid[5] = True
    
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    if re.search(r"[0-9]{9}",pass_dict['pid']) and len(pass_dict['pid'])==9: 
        pass_valid[6] = True
        
    #cid (Country ID) - ignored, missing or not.
            
    if not False in pass_valid:
        return True
    else:
        return False

def count_valid_passports(pass_list,debug=DEBUG):
    valid_passports = 0
    for pass_dict in pass_list:
        if check_passport_simple(pass_dict,debug=debug) and check_passport_with_validation(pass_dict):
            valid_passports += 1
    return valid_passports

if __name__=="__main__":
    pass_input = load_input()
    pass_list = parse_passport_file(pass_input, DEBUG)
    good_passports = count_valid_passports(pass_list)

    print(f"Part1: Anzahl gültiger Pässe {good_passports}")
    