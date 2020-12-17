#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


DAY = 16


PUZZLE = f"t{DAY}puzzle.input"
EXAMPLE = f"t{DAY}puzzle.example"
EXAMPLE2 = f"t{DAY}puzzle.example2"

range_with_endpoint = lambda low, high: range(low,high+1)

def load_input(filename = EXAMPLE ):
    with open(filename,"r") as file:
        rules,my_ticket,other_tickets = file.read().split("\n\n")

    rule_dict = {rulename:[range_with_endpoint(*list(map(int,rule.split("-")))) for rule in rulevalues.strip().split(" or ")] for rulename,rulevalues in 
                           (ruleset.split(":") for ruleset in rules.split("\n"))
                           }
    
    myticket_values = [int(elem) for elem in my_ticket.split("\n")[1].split(",")]
    other_ticket_values = np.array([line.split(",") for line in other_tickets.strip().split("\n")[1:]],dtype=int)
    
    return rule_dict,myticket_values,other_ticket_values
 
check_any_rules = lambda value, some_rules: any([((value in rule_low) or (value in rule_high)) for rule_low, rule_high in some_rules])


def validate_tickets(rules,tickets):
    bad_numbers = []
    good_tickets = []
    for ticket in tickets:
        check_list = [check_any_rules(value,rules.values()) for value in ticket]
        if all(check_list):
            good_tickets.append(ticket)
        else:
            for pos,ok in enumerate(check_list):
                if not ok:
                    bad_numbers.append(ticket[pos])
    
    print(f"Part1: The sum of the bad numbers is {sum(bad_numbers)}")
    return good_tickets

check_rule = lambda value, some_rule: any([value in rule_range for rule_range in some_rule])


def determine_ticket_fields(rules, tickets,verbose=False):
    ticket_cols = np.array(tickets).transpose()
    ticket_dict = {}
    while len(rules):
        next_ticket_cols = [False for elem in ticket_cols]
        for row_nr,row_set in enumerate(ticket_cols):
            if row_set.__class__ == bool:
                continue
            possible_rules = []
            for rule_name, rule_set in rules.items():
                if all([check_rule(value, rule_set) for value in row_set]):
                    possible_rules.append(rule_name)
            if len(possible_rules)==1:
                if verbose:
                    print(f"  The Rule {possible_rules[0]} was identified at position {row_nr}.")
                ticket_dict[row_nr] = possible_rules[0]
                rules.pop(possible_rules[0])
            else: 
                if verbose:
                    print(f"    Found {len(possible_rules)} candidates for position {row_nr}: ",",".join(possible_rules))
                next_ticket_cols[row_nr]=row_set
        ticket_cols = next_ticket_cols.copy()
        
        if len(rules) and verbose:
            print("Another round. Found so far:", ticket_dict)
    
    if verbose:
        print("Finally: ",ticket_dict)
    return ticket_dict

if __name__=="__main__":
    pass
    rule_dict, my_ticket, other_tickets = load_input(PUZZLE)
    good_tickets = validate_tickets(rule_dict,other_tickets)
    
    ticket_dict = determine_ticket_fields(rule_dict, good_tickets)
    print("My Ticket tells me:")
    magic_number = 1
    for pos, value in enumerate(my_ticket):
        if "departure" in ticket_dict[pos]:
            magic_number *= value
        print(f"{magic_number} - {ticket_dict[pos]}: {value}")
    print(f"Part2: {magic_number}")