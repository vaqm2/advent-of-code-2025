#!/usr/bin/env python3

def main() -> None:
    with open("/input/input_day5.txt") as f:
        database = f.read().strip()
    fresh, available = database.split("\n\n")
    available_items = set(map(int, available.split("\n")))
    num_fresh_available = 0
    fresh_ranges = []
    for range_str in fresh.split("\n"):
        fresh_range_start, fresh_range_end = map(int, range_str.split("-"))
        fresh_ranges.append((fresh_range_start, fresh_range_end))
        for i in available_items.copy():
            if i >= fresh_range_start and i <= fresh_range_end:
                num_fresh_available += 1
                available_items.remove(i)
    fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    current_start = fresh_ranges[0][0]
    current_end = fresh_ranges[0][1]
    num_fresh = 0
    for range_idx in range(1, len(fresh_ranges)):
        if fresh_ranges[range_idx][0] <= current_end:
            current_end = max(current_end, fresh_ranges[range_idx][1])
        else:
            num_fresh += current_end - current_start + 1
            current_start = fresh_ranges[range_idx][0]
            current_end = fresh_ranges[range_idx][1]
    num_fresh += current_end - current_start + 1
    
    print(num_fresh, num_fresh_available)
            

if __name__ == "__main__":
    main()