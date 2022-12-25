#!/usr/bin/python
from typing import Dict, List, Tuple, Set
import collections


class Volcano:
    def __init__(self, flows: Dict[str, int], paths: Dict[str, List[str]]) -> None:
        self._flows = flows
        self._paths = paths
        self._shortest_paths: Dict[Tuple[str, str], List[str]] = {}
        self._valves_to_open: List[str] = []
        self._all_valves_bitmask = 0

    def solve(self) -> int:
        self._paths_bfs()
        self._set_valves_to_open()
        max_flow = 0
        for subset in range(2**len(self._valves_to_open)):
            my_valves = set()
            elephant_valves = set()
            for i, valve in enumerate(self._valves_to_open):
                if subset & (1<<i):
                    my_valves.add(valve)
                else:
                    elephant_valves.add(valve)
            if len(elephant_valves) > len(my_valves):
                continue  # we can ignore it because of problem symmetry
            my_flow = self._find_max_flow("AA", 0, my_valves, 26)
            elephant_flow = self._find_max_flow("AA", 0, elephant_valves, 26)
            max_flow = max(max_flow, my_flow + elephant_flow)
        return max_flow

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
        self._all_valves_bitmask = 2**len(self._valves_to_open) - 1

    # _find_max_flow recursively finds max flow
    def _find_max_flow(self, position: str, flow_speed: int, valves_to_open: Set[str], time_left: int) -> int:
        max_flow = flow_speed * time_left  # case in which we do not open any more valves
        # split problem into:
        # - get to one of the valves_to_open and open it (calculate flow in the meantime)
        # - recursively call _find_max_flow with one more valve in open_valves and less time_left
        new_valves_to_open = valves_to_open.copy()
        for valve in valves_to_open:
            time_to_open = len(self._shortest_paths[(position, valve)]) + 1
            if time_to_open > time_left:
                continue
            flow_until_new_open = flow_speed * time_to_open
            new_time_left = time_left - time_to_open
            new_flow_speed = flow_speed + self._flows[valve]
            new_valves_to_open.remove(valve)
            flow_after_new_open = self._find_max_flow(valve, new_flow_speed, new_valves_to_open, new_time_left)
            new_valves_to_open.add(valve)
            flow = flow_until_new_open + flow_after_new_open
            max_flow = max(max_flow, flow)
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

