#!/usr/bin/env python3

import re
from pprint import pprint

def toggle_switch(indiactor_light: str) -> str:
    if indiactor_light == ".":
        return "#"
    return "."

def to_binary(switches: list[str], length: int) -> list[list[int]]:
    switches_binary = []
    for switch in switches:
        binary_switch = [0] * length
        indices = [int(i) for i in switch.split(",")]
        for index in indices:
            binary_switch[index] = 1
        switches_binary.append(binary_switch)
    return switches_binary

def gaussian_elimination_gf2(switches: list[list[int]], target: list[int]) -> int | None:
    num_switches = len(switches)
    num_lights = len(target)

    # Build augmented matrix [switches | target]
    augmented_matrix = []
    for light in range(num_lights):
        row = []
        for switch in switches:
            row.append(switch[light])
        row.append(target[light])
        augmented_matrix.append(row)

    current_light = 0  # Current pivot row
    cols_with_pivots = []

    # Forward elimination - create row echelon form
    for switch_num in range(num_switches):
        # Find a row with 1 in this column (pivot)
        pivot_found = False
        for light_num in range(current_light, num_lights):
            if augmented_matrix[light_num][switch_num] == 1:
                # Swap rows to bring pivot to current_light position
                augmented_matrix[current_light], augmented_matrix[light_num] = \
                    augmented_matrix[light_num], augmented_matrix[current_light]
                pivot_found = True
                break
        
        if not pivot_found:
            # No pivot in this column, skip it (free variable)
            continue
        
        cols_with_pivots.append(switch_num)
        
        # Eliminate this column in all OTHER rows (make them 0)
        for light_num in range(num_lights):
            if light_num != current_light and augmented_matrix[light_num][switch_num] == 1:
                # XOR this row with pivot row to eliminate
                for col in range(num_switches + 1):  # +1 for target column
                    augmented_matrix[light_num][col] ^= augmented_matrix[current_light][col]
        
        current_light += 1
    
    # Check for inconsistencies (impossible cases like 0 = 1)
    for light_num in range(current_light, num_lights):
        all_switches_zero = all(augmented_matrix[light_num][col] == 0 for col in range(num_switches))
        target_is_one = augmented_matrix[light_num][-1] == 1
        
        if all_switches_zero and target_is_one:
            # Row says: 0*S0 + 0*S1 + ... = 1, which is impossible
            return None
    
    # Find free variables (switches without pivots)
    pivot_set = set(cols_with_pivots)
    free_vars = [i for i in range(num_switches) if i not in pivot_set]
    
    # Try all combinations of free variables to find minimum
    min_switches = float('inf')
    
    for mask in range(1 << len(free_vars)):  # 2^(number of free vars) combinations
        solution = [0] * num_switches
        
        # Set free variables according to mask
        for i, free_var in enumerate(free_vars):
            solution[free_var] = (mask >> i) & 1
        
        # Back substitution - solve for pivot variables
        for i in range(len(cols_with_pivots) - 1, -1, -1):
            switch_num = cols_with_pivots[i]
            light_num = i
            
            # solution[switch_num] = target XOR (contributions from other switches)
            val = augmented_matrix[light_num][-1]
            for col in range(switch_num + 1, num_switches):
                val ^= (augmented_matrix[light_num][col] & solution[col])
            solution[switch_num] = val
        
        # Count switches used in this solution
        num_used = sum(solution)
        min_switches = min(min_switches, num_used)
    
    return min_switches if min_switches != float('inf') else None

def get_fewest_switches(desired_status: str, switches: list[str]) -> int:
    initial_status = "." * len(desired_status)
    difference = [0 if x == y else 1 for x, y in zip(initial_status, desired_status)]
    switches_binary = to_binary(switches, len(desired_status))
    fewest_switches = float("inf")
    return gaussian_elimination_gf2(switches_binary, difference)


def main() -> None:
    fewest_switches = 0
    with open("input/input_day10.txt", encoding="utf-8") as file:
        for line in file:
            line_contents = line.split()
            indicator_lights = line_contents[0].replace("[", "").replace("]", "")
            switches = [switch.replace("(", "").replace(")", "") for switch in line_contents[1:-1]]
            joltage = line_contents[-1].replace("{", "").replace("}", "")
            fewest_switches += get_fewest_switches(indicator_lights, switches)
    print(fewest_switches)

if __name__ == "__main__":
    main()