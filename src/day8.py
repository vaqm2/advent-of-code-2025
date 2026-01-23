#!/usr/bin/env python3

from __future__ import annotations
from pprint import pprint
from typing import List, Tuple

class Circuits:
    def __init__(self) -> None:
        self.roots = {}
        self.circuit_sizes = {}
        self.last_added = None

    def find_root(self, point: Tuple[int, int, int]) -> Tuple[int, int, int]:
        if point in self.roots:
            if self.roots[point] != point:
                self.roots[point] = self.find_root(self.roots[point])
            return self.roots[point]
        else:
            self.roots[point] = point
            self.circuit_sizes[point] = 1
            return point

    def are_connected(self, point1: Tuple[int, int, int], point2: Tuple[int, int, int]) -> bool:
        return self.find_root(point1) == self.find_root(point2)

    def connect(self, point1: Tuple[int, int, int], point2: Tuple[int, int, int]) -> None:
        point1_root = self.find_root(point1)
        point2_root = self.find_root(point2)
        self.roots[point2_root] = point1_root
        self.circuit_sizes[point1_root] += self.circuit_sizes[point2_root]
        del self.circuit_sizes[point2_root]
        self.last_added = (point1, point2)

    def get_circuit_sizes(self) -> List[int]:
        return sorted(list(self.circuit_sizes.values()), reverse=True)

def calculate_distance(x: Tuple[int, int, int], y: Tuple[int, int, int]) -> float:
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2) ** 0.5

def main() -> None:
    with open("input/input_day8.txt") as f:
        junction_box_coordinates = f.read().strip().splitlines()

    distances = []
    for i in range(len(junction_box_coordinates)):
        coord1 = tuple(map(int, junction_box_coordinates[i].split(",")))
        for j in range(i + 1, len(junction_box_coordinates)):
            coord2 = tuple(map(int, junction_box_coordinates[j].split(",")))
            dist = calculate_distance(coord1, coord2)
            distances.append({
                "point1": coord1,
                "point2": coord2,
                "distance": dist
            })
    distances.sort(key=lambda x: x["distance"])

    circuits_part1 = Circuits()
    circuits_part2 = Circuits()

    for edges in distances[:1000]:
        if circuits_part1.are_connected(edges["point1"], edges["point2"]):
            continue
        circuits_part1.connect(edges["point1"], edges["point2"])

    product = 1
    for size in circuits_part1.get_circuit_sizes()[:3]:
        product *= size
    
    print("Solution Part 1:", product)

    for edges in distances:
        if circuits_part2.are_connected(edges["point1"], edges["point2"]):
            continue
        circuits_part2.connect(edges["point1"], edges["point2"])
    
    print(f"Solution: {circuits_part2.last_added[0][0] * circuits_part2.last_added[1][0]}")

if __name__ == "__main__":
    main()