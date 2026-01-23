#!/usr/bin/env python3


class Node:
    def __init__(self, name: str):
        self.name = name
        self.gets_from = []
        self.gives_to = []

    def add_giver(self, node: "Node") -> None:
        self.gets_from.append(node)

    def add_getter(self, node: "Node") -> None:
        self.gives_to.append(node)

    def __repr__(self) -> str:
        return f"""Node({self.name},
        gets_from={[node.name for node in self.gets_from]},
        gives_to={[node.name for node in self.gives_to]})"""


def count_paths(
    start: Node, end: Node, via: set[Node] | None = None, visited: set[Node] | None = None, cache: dict | None = None
) -> int:
    if cache is None:
        cache = {}
    key = (
        start.name,
        frozenset(via) if via else None,
        frozenset(via) & frozenset(visited) if visited and via else None,
    )
    if key in cache:
        return cache[key]
    if visited is None:
        visited = set()
    if start in visited:
        return 0
    visited.add(start)
    num_paths = 0
    for getter in start.gives_to:
        if getter == end:
            if via is None or len(via) == 0:
                num_paths += 1
            else:
                if via == visited & via:
                    num_paths += 1
            continue
        else:
            num_paths += count_paths(getter, end, via, visited.copy(), cache)
    cache[key] = num_paths
    return num_paths


def main() -> None:
    with open("input/input_day11.txt", encoding="utf-8") as f:
        nodes = {}
        for line in f.read().splitlines():
            parent, children = line.split(":")
            parent = parent.strip()
            children = [child.strip() for child in children.split() if child.strip()]
            parent_node = nodes.get(parent, Node(parent))
            for child_name in children:
                child_node = nodes.get(child_name, Node(child_name))
                parent_node.add_getter(child_node)
                child_node.add_giver(parent_node)
                nodes[child_name] = child_node
            nodes[parent] = parent_node
    if "out" in nodes:
        out_node = nodes.get("out")
    if "you" in nodes:
        you_node = nodes.get("you")
        if out_node is not None and you_node is not None:
            print(count_paths(you_node, out_node, via=None))
    if "dac" in nodes:
        dac_node = nodes.get("dac")
    if "fft" in nodes:
        fft_node = nodes.get("fft")
    if "svr" in nodes:
        svr_node = nodes.get("svr")
    if dac_node is not None and fft_node is not None and svr_node is not None and out_node is not None:
        print(count_paths(svr_node, out_node, {dac_node, fft_node}))


if __name__ == "__main__":
    main()
