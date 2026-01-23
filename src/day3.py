#!/usr/bin/env python3


def max_power(ratings: str) -> int:
    max_rating = 0
    ratings_list = [int(x) for x in ratings]
    max_value_index = -1
    for n in range(12, 0, -1):
        max_value = max(ratings_list[0:len(ratings_list)-(n-1)])
        max_value_index = ratings_list.index(max_value)
        max_rating = max_rating + max_value * 10**(n-1)
        ratings_list = ratings_list[max_value_index+1:]
    return max_rating

def main() -> None:
    total_power = 0
    with open("/input/input_day3.txt") as f:
        power_banks = [line.strip() for line in f.readlines()]
    for power_bank_ratings in power_banks:
        total_power += max_power(power_bank_ratings)
    print(f"Total Power: {total_power}")


if __name__ == "__main__":
    main()