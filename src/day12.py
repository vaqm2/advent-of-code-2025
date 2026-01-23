#!/usr/bin/env python3

from pprint import pprint


def rotate_present(present: list[list[str]]) -> list[list[str]]:
    nrows = len(present)
    ncols = len(present[0]) if nrows > 0 else 0
    rotated = [["." for _ in range(nrows)] for _ in range(ncols)]
    for r in range(nrows):
        for c in range(ncols):
            rotated[c][nrows - 1 - r] = present[r][c]
    return rotated


def can_fit_all(nrows: int, ncols: int, required_presents: list[list[str]]) -> bool:
    if required_presents == []:
        return True
    return False


def main() -> None:
    presents = {}
    num_fitting = 0
    with open("input/test_day12.txt", encoding="utf-8") as f:
        input = f.read().split("\n\n")
    for line in input[0:-1]:
        line = line.replace("#", "1").replace(".", "0")
        index = line.split("\n")[0]
        index = index.replace(":", "")
        present = line.split("\n")[1:]
        present = [list(row) for row in present if row.strip()]
        for i in range(len(present)):
            for j in range(len(present[0])):
                present[i][j] = int(present[i][j])
        presents[index] = present
    for line in input[-1].splitlines():
        size, required = line.split(":")
        size = size.strip()
        required = required.strip()
        nrows, ncols = [int(x) for x in size.split("x") if x.strip()]
        required_presents = []
        for item_index, count in enumerate(required.split()):
            for _ in range(int(count)):
                present = presents[str(item_index)]
                required_presents.append(present)
        num_fitting += can_fit_all(nrows, ncols, required_presents)
    print(f"Number of regions that can fit presents: {num_fitting}")


if __name__ == "__main__":
    main()
