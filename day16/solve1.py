#!/usr/bin/python
from typing import Dict, List

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
    # TODO do a proper solution, this is just naive greedy search
    total_flow = 0
    position = "AA"
    opened_valves = set()
    for time in range(1, 31):
        flow = flows[position]
        if flow == 0 or position in opened_valves:
            children = paths[position]
            if len(children) == 0:
                print(f"stuck at valve {position}")
                break
            greedy_best_child = ""
            child_best_flow = -1
            for c in children:
                if c in opened_valves:
                    continue
                if flows[c] > child_best_flow:
                    greedy_best_child = c
                    child_best_flow = flows[c]
            if greedy_best_child:
                position = greedy_best_child
                print(f"move to {position}")
            else:
                print(f"stuck at valve {position}")
                break
        else:
            print(f"open valve {position}")
            opened_valves.add(position)
            total_flow += flow * (30 - time)
    print(f"naive greedy solution: {total_flow}")


if __name__ == "__main__":
    main()

