#!/usr/bin/python
import math
from typing import List, Dict
from collections import namedtuple, defaultdict


StateFields = ("ore_robots", "clay_robots", "obsidian_robots", "geode_robots", "ore", "clay", "geode", "obsidian", "time_left")
State = namedtuple("State", StateFields, defaults=(0,)*len(StateFields))
RobotIndexByResource = {
    "ore": 0,
    "clay": 1,
    "obsidian": 2,
    "geode": 3,
}
RobotResourceByIndex = ["ore", "clay", "obsidian", "geode"]


# can_always_build checks if resources we have now and we are going to produce
# are enough to cover given cost each minute
def can_always_build(state: State, costs: Dict[str, int]) -> bool:
    for resource, cost in costs.items():
        robots_count = state[RobotIndexByResource[resource]]
        if robots_count < cost:
            return False
        if getattr(state, resource) < cost:
            return False
    return True


class Blueprint:
    def __init__(self, costs: List[int]):
        self._number = costs[0]
        self._costs = [
            {
                "ore": costs[1],
                "clay": 0,
                "obsidian": 0,
            },
            {
                "ore": costs[2],
                "clay": 0,
                "obsidian": 0,
            },
            {
                "ore": costs[3],
                "clay": costs[4],
                "obsidian": 0,
            },
            {
                "ore": costs[5],
                "clay": 0,
                "obsidian": costs[6],
            },
        ]
        self._max_costs = [0] * 3
        # We can build only 1 robot per turn and our goal is to maximize geodes count.
        # Ore, clay and obsidian are just means to getting geode robots, so max
        # useful ore/clay/obsidian robots count is max cost in given resource.
        for robot_costs in self._costs:
            for resource, cost in robot_costs.items():
                i = RobotIndexByResource[resource]
                self._max_costs[i] = max(self._max_costs[i], cost)

    # count_max_geodes uses brutal DFS with good pruning heuristics
    def count_max_geodes(self, time_left: int) -> int:
        state0 = State(ore_robots=1, time_left=time_left)
        stats = defaultdict(lambda: 0)  # just to show statistics of search pruning etc.
        result = 0
        states = [state0]
        max_geodes_by_time_left = [0] * (state0.time_left + 1)
        while len(states) > 0:
            state = states.pop()
            if state.time_left <= 0:
                result = max(result, state.geode)
                max_geodes_by_time_left[0] = max(max_geodes_by_time_left[0], state.geode)
                stats["out of time"] += 1
                continue
            # max_geodes can be reached if we build geode robot each turn.
            # In this case max geodes count will be a sum of an arithmetic sequence.
            max_geode_robots = state.geode_robots + state.time_left - 1
            max_geodes = state.geode + (state.geode_robots + max_geode_robots) * state.time_left // 2
            # Skip if we already explored a branch with more geodes than optimisitc max geodes count in current state
            if max_geodes_by_time_left[state.time_left] > max_geodes:
                stats["max prunes"] += 1
                continue
            # If we have so many robots that we can always build geode robot, we can end now
            if can_always_build(state, self._costs[3]):
                result = max(result, max_geodes)
                max_geodes_by_time_left[state.time_left] = max(max_geodes_by_time_left[state.time_left], max_geodes)
                stats["arithmetic sequence"] += 1
                continue
            # Subproblems if we try to build one of the robots:
            robots_built = 0
            for robot_index, costs in enumerate(self._costs):
                robots_count = state[robot_index]
                if robot_index < 3:  # ore/clay/obsidian
                    if robots_count >= self._max_costs[robot_index]:
                        # there is no point in building given robot
                        continue
                time_until_building_robot = 0
                for resource, cost in costs.items():
                    diff = cost - getattr(state, resource)
                    if diff <= 0:
                        continue  # we have enough of given resource to build robot now
                    miners = state[RobotIndexByResource[resource]]
                    if diff > 0 and miners == 0:
                        time_until_building_robot = state.time_left  # it means we will never get resources for that robot
                        break
                    time_until_building_robot = max(time_until_building_robot, math.ceil(diff / miners))
                if time_until_building_robot >= state.time_left:
                    continue
                new_robots = [state[i] + 1 if i == robot_index else state[i] for i in range(4)]
                t = time_until_building_robot + 1
                new_state = State(
                    ore_robots=new_robots[0],
                    clay_robots=new_robots[1],
                    obsidian_robots=new_robots[2],
                    geode_robots=new_robots[3],
                    ore=state.ore + t*state.ore_robots - costs["ore"],
                    clay=state.clay + t*state.clay_robots - costs["clay"],
                    obsidian=state.obsidian + t*state.obsidian_robots - costs["obsidian"],
                    geode=state.geode + t*state.geode_robots,
                    time_left=state.time_left - t,
                )
                states.append(new_state)
                robots_built += 1
            # If we cannot build anything until whole time left - end
            if robots_built == 0:
                max_geodes = state.geode + state.geode_robots * state.time_left
                result = max(result, max_geodes)
                max_geodes_by_time_left[state.time_left] = max(max_geodes_by_time_left[state.time_left], max_geodes)
                stats["cannot build"] += 1
        stats_str = ", ".join(f"{key}: {value}" for key, value in stats.items())
        print(f"{self._number} count_max_geodes({time_left})={result} (stats: {stats_str})")
        return result

    def quality_level(self, time_left: int) -> int:
        return self._number * self.count_max_geodes(time_left)
    
    def __str__(self) -> str:
        return f"{self._number}: costs {self._costs}, max costs {self._max_costs}"


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
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if not line:
                    continue
                blueprints.append(Blueprint(all_ints_from_str(line)))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    print("part1", sum(bp.quality_level(24) for bp in blueprints))
    result = 1
    for bp in blueprints[:3]:
        result *= bp.count_max_geodes(32)
    print("part2", result)


if __name__ == "__main__":
    main()
