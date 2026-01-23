#!/usr/bin/env python3

from pprint import pprint

def calculate_area(corner1: tuple[int, int], corner2: tuple[int, int]) -> int:
    """Calculate area of rectangle inclusive of both corners."""
    width = abs(corner2[0] - corner1[0]) + 1
    height = abs(corner2[1] - corner1[1]) + 1
    return width * height


def main() -> None:
    red_tiles = set()
    green_tiles = set()
    max_area = 0
    red_tiles_by_x = {}
    red_tiles_by_y = {}

    with open("input/input_day9.txt") as f:
        for line in f.readlines():
            x, y = map(int, line.strip().split(","))
            red_tiles.add((x, y))
            red_tiles_by_x.setdefault(x, set()).add(y)
            red_tiles_by_y.setdefault(y, set()).add(x)

    

    valid_tiles = red_tiles.union(green_tiles)
    red_list = list(red_tiles)
    for i, (x1, y1) in enumerate(red_list):
        for (x2, y2) in red_list[i+1:]:
            if x1 == x2 or y1 == y2:
                continue
            
            corner12 = (x1, y2)
            corner21 = (x2, y1)
            if corner12 in valid_tiles and corner21 in valid_tiles:
                area = calculate_area((x1, y1), (x2, y2))
                if area > max_area:
                    max_area = area
    
    print(f"Maximum area of rectangle: {max_area}")
            

if __name__ == "__main__":
    main()