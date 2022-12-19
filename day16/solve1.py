#!/usr/bin/python
from typing import Dict, List, Tuple, Set
import collections
import itertools


class Volcano:
    def __init__(self, flows: Dict[str, int], paths: Dict[str, List[str]]) -> None:
        self._flows = flows
        self._paths = paths
        self._shortest_paths: Dict[Tuple[str, str], List[str]] = {}
        self._valves_to_open: List[str] = []

    def solve(self) -> int:
        # TODO do a proper solution, this has too large complexity -
        # O(N!), N being the number of valves with nonzero flow.
        # It works in reasonable time only for data_small.txt.
        self._paths_bfs()
        self._set_valves_to_open()
        return self._brute_force_solve()

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

    def _brute_force_solve(self) -> int:
        best_total_flow = 0
        best_valves_order = None
        for valves in itertools.permutations(self._valves_to_open):
            total_flow = self._brute_force_iteration(valves)
            if total_flow > best_total_flow or best_valves_order is None:
                best_total_flow = total_flow
                best_valves_order = valves
        print(f"brute force - best order for {best_valves_order}")
        self._verbose_brute_force_iteration(best_valves_order)  # do it once again just to follow what is going on
        return best_total_flow

    def _verbose_brute_force_iteration(self, valves: Tuple[str]) -> int:
        print(f"running verbose brute force for {valves}")
        total_flow = 0
        position = "AA"
        next_valve_to_open_index = 0
        next_valve_to_open = valves[0]
        for time in range(1, 31):
            if position == next_valve_to_open:
                print(f"  opened valve {position} after minute {time}")
                total_flow += self._flows[position] * (30 - time)
                next_valve_to_open_index += 1
                if next_valve_to_open_index >= len(valves):
                    print(f"  all important valves already opened after minute {time}")
                    break
                next_valve_to_open = valves[next_valve_to_open_index]
            else:
                next_valve = self._shortest_paths[(position, next_valve_to_open)][0]
                print(f"  moved from {position} to {next_valve} afer minute {time}")
                position = next_valve
        return total_flow

    def _brute_force_iteration(self, valves: Tuple[str]) -> int:
        total_flow = 0
        position = "AA"
        next_valve_to_open_index = 0
        next_valve_to_open = valves[0]
        for time in range(1, 31):
            if position == next_valve_to_open:
                total_flow += self._flows[position] * (30 - time)
                next_valve_to_open_index += 1
                if next_valve_to_open_index >= len(valves):
                    break
                next_valve_to_open = valves[next_valve_to_open_index]
            else:
                next_valve = self._shortest_paths[(position, next_valve_to_open)][0]
                position = next_valve
        return total_flow


def main():
    flows: Dict[str, int] = {}
    paths: Dict[str, List[str]] = {}
    with open("data_small.txt", "r") as f:
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

