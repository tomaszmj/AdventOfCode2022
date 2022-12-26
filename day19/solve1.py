#!/usr/bin/python
from typing import List, Dict
from collections import namedtuple


StateFields = ("ore_robots", "clay_robots", "obsidian_robots", "geode_robots", "ore", "clay", "obsidian", "time_left")
State = namedtuple("State", StateFields, defaults=(0,)*len(StateFields))


class Blueprint:
    def __init__(self, costs: List[int]):
        self._costs = [
            {
                "ore": costs[0],
                "clay": 0,
                "obsidian": 0,
            },
            {
                "ore": costs[1],
                "clay": 0,
                "obsidian": 0,
            },
            {
                "ore": costs[2],
                "clay": costs[3],
                "obsidian": 0,
            },
            {
                "ore": costs[4],
                "clay": 0,
                "obsidian": costs[5],
            },
        ]

    def count_max_geodes(self) -> int:
        state = State(ore_robots=1, time_left=12)
        return self._max_geodes(state, {})

    def _max_geodes(self, state: State, store: Dict[State, int]) -> int:
        if state in store:
            return store[state]
        # print(f"_max_geodes({state})")
        geodes = 0
        if state.time_left == 1:
            store[state] = state.geode_robots
            return state.geode_robots

        # if we do not build new robots:
        new_state = State(
            ore_robots=state.ore_robots,
            clay_robots=state.clay_robots,
            obsidian_robots=state.obsidian_robots,
            geode_robots=state.geode_robots,
            ore=state.ore+state.ore_robots,
            clay=state.clay+state.clay_robots,
            obsidian=state.obsidian+state.obsidian_robots,
            time_left=state.time_left-1,
        )
        geodes = max(geodes, state.geode_robots + self._max_geodes(new_state, store))

        # if we try to build a robot:
        for robot_index, costs in enumerate(self._costs):
            can_build = True
            for resource, cost in costs.items():
                if getattr(state, resource) < cost:
                    can_build = False
                    break
            if can_build:
                new_robots = [state[i] + 1 if i == robot_index else state[i] for i in range(4)]
                new_state = State(
                    ore_robots=new_robots[0],
                    clay_robots=new_robots[1],
                    obsidian_robots=new_robots[2],
                    geode_robots=new_robots[3],
                    ore=state.ore-costs["ore"]+state.ore_robots,
                    clay=state.clay-costs["clay"]+state.clay_robots,
                    obsidian=state.obsidian-costs["obsidian"]+state.obsidian_robots,
                    time_left=state.time_left-1,
                )
                geodes = max(geodes, state.geode_robots + self._max_geodes(new_state, store))
        store[state] = geodes
        return geodes


def all_ints_from_str(s: str) -> List[int]:
    numbers = []
    number_begin = -1
    for i, c in enumerate(s):
        isnumeric = c.isdigit() or (c == "-" and i < len(s) - 1 and s[i+1].isdigit())
        if isnumeric and number_begin == -1:
            number_begin = i
        elif not isnumeric and number_begin >= 0:
            numbers.append(int(s[number_begin:i]))
            number_begin = -1
    if number_begin >= 0:
        numbers.append(int(s[number_begin:len(s)]))
    return numbers


def main():
    blueprints = []
    with open("data_small.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if not line:
                    continue
                blueprints.append(Blueprint(all_ints_from_str(line[1:])))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    for i, bp in enumerate(blueprints):
        print(f"{i}: {bp.count_max_geodes()}")


if __name__ == "__main__":
    main()

