#!/usr/bin/python
from typing import Dict, List, Tuple
import collections


class Volcano:
    def __init__(self, flows: Dict[str, int], paths: Dict[str, List[str]]) -> None:
        self._flows = flows
        self._paths = paths
        self._shortest_paths: Dict[Tuple[str, str], List[str]] = {}
        self._valves_to_open: List[str] = []

    def solve(self) -> int:
        self._paths_bfs()
        self._set_valves_to_open()
        return self._find_max_flow("AA", 0, 30, {})

    def _paths_bfs(self):
        self._shortest_paths = {}
        for start in self._paths.keys():
            to_check = collections.deque([(start, None)])  # (valve, predecessor)
            visited = {start}
            while len(to_check) > 0:
                valve, predecessor = to_check.popleft()
                if predecessor is not None:
                    self._shortest_paths[(start, valve)] = self._shortest_paths[(start, predecessor)] + [valve]
                else:
                    self._shortest_paths[(start, valve)] = []
                for child in self._paths[valve]:
                    if child in visited:
                        continue
                    visited.add(child)
                    to_check.append((child, valve))

    def _set_valves_to_open(self):
        self._valves_to_open = []
        for valve, flow in self._flows.items():
            if flow > 0:
                self._valves_to_open.append(valve)

    # _find_max_flow recursively finds max flow using dynamic programming
    def _find_max_flow(self, position: str, open_valves_subset: int, time_left: int, store: dict) -> int:
        key = (position, open_valves_subset, time_left)
        if key in store:
            # print(f"_find_max_flow({key}) -> {store[key]} from store")
            return store[key]
        # print(f"_find_max_flow({key}) ...")
        open_valves = set()
        valves_to_open = {}
        current_flow = 0
        for i, valve in enumerate(self._valves_to_open):
            bitmask = 1<<i
            if bitmask & open_valves_subset:
                open_valves.add(valve)
                current_flow += self._flows[valve]
            else:
                valves_to_open[valve] = bitmask
        max_flow = current_flow * time_left
        for valve in valves_to_open:
            time_to_open = len(self._shortest_paths[(position, valve)]) + 1
            if time_to_open > time_left:
                continue
            flow_until_new_open = current_flow * time_to_open
            new_time_left = time_left - time_to_open
            new_open_valves_subset = open_valves_subset | valves_to_open[valve]
            flow_after_new_open = self._find_max_flow(valve, new_open_valves_subset, new_time_left, store)
            flow = flow_until_new_open + flow_after_new_open
            max_flow = max(max_flow, flow)
        store[key] = max_flow
        # print(f"... _find_max_flow({key}) -> {max_flow}")
        return max_flow


def main():
    flows: Dict[str, int] = {}
    paths: Dict[str, List[str]] = {}
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                spl = line.split(" ")
                valve = spl[1]
                rate_str = spl[4]
                _, _, rate_str = rate_str.partition("rate=")
                leads_to = [s.rstrip(",") for s in spl[9:]]
                flows[valve] = int(rate_str[:-1])
                paths[valve] = leads_to
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    volcano = Volcano(flows, paths)
    print(volcano.solve())


if __name__ == "__main__":
    main()

