#!/usr/bin/env python3


def main() -> None:
    with open("input/input_day7.txt", encoding="utf-8") as f:
        manifold = f.read()
    manifold_list = [list(line) for line in manifold.splitlines()]
    beam_positions = {manifold_list[0].index("S")}
    active_layer = {manifold_list[0].index("S"): 1}
    num_splits = 0
    for row in manifold_list[1:]:
        next_layer: [int, int] = {}
        for index in beam_positions.copy():
            char = row[index]
            if char == "^":
                num_splits += 1
                beam_positions.remove(index)
                if row[index - 1] == ".":
                    beam_positions.add(index - 1)
                    next_layer.setdefault(index - 1, 0)
                    next_layer[index - 1] += active_layer.get(index, 0)
                if row[index + 1] == ".":
                    beam_positions.add(index + 1)
                    next_layer.setdefault(index + 1, 0)
                    next_layer[index + 1] += active_layer.get(index, 0)
            else:
                if index in active_layer:
                    next_layer[index] = next_layer.get(index, 0) + active_layer[index]
        active_layer = next_layer

    num_timelines = sum(active_layer.values())
    print(f"Part 1: {num_splits}")
    print(f"Part 2: {num_timelines}")


if __name__ == "__main__":
    main()
