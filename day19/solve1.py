#!/usr/bin/python
from typing import List, Dict
from collections import namedtuple, defaultdict


StateFields = ("ore_robots", "clay_robots", "obsidian_robots", "geode_robots", "ore", "clay", "obsidian", "time_left")
State = namedtuple("State", StateFields, defaults=(0,)*len(StateFields))
RobotIndexByResource = {
    "ore": 0,
    "clay": 1,
    "obsidian": 2,
    "geode": 3,
}
RobotResourceByIndex = ["ore", "clay", "obsidian", "geode"]


# can_build_now checks if resources we have now are enough to cover given cost
def can_build_now(state: State, costs: Dict[str, int]) -> bool:
    for resource, cost in costs.items():
        if getattr(state, resource) < cost:
            return False
    return True


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
        self._store: Dict[State, int] = {}


    def count_max_geodes(self, time_left: int) -> int:
        stats = defaultdict(lambda: 0)
        state = State(ore_robots=1, time_left=time_left)
        max_so_far_by_time_left = [0]*time_left
        result = self._max_geodes(state, max_so_far_by_time_left, stats)
        stats_str = ", ".join(f"{key}: {value}" for key, value in stats.items())
        print(f"{self._number} count_max_geodes({time_left}) = {result} (stats {stats_str})")
        return result

    def quality_level(self, time_left: int) -> int:
        return self._number * self.count_max_geodes(time_left)

    def _max_geodes(self, state: State, max_so_far_by_time_left: List[int], stats: Dict[str, int]) -> int:
        if state in self._store:
            stats["lookups"] += 1
            return self._store[state]
        for resource in RobotResourceByIndex[:3]:
            key = "max_" + resource
            stats[key] = max(stats[key], getattr(state, resource))
        geodes = 0
        if state.time_left == 1:
            self._store[state] = state.geode_robots
            stats["out of time"] += 1
            return state.geode_robots
        
        # If we have so many robots that we can always build geode robot,
        # we can maximize geodes count by simply building geode robot each turn.
        # In this case max geodes count will be a sum of an arithmetic sequence.
        if can_always_build(state, self._costs[3]):
            max_geode_robots = state.geode_robots + state.time_left - 1
            optimisitc_max_geodes = (state.geode_robots + max_geode_robots) * state.time_left // 2
            self._store[state] = optimisitc_max_geodes
            stats["arithmetic sequence"] += 1
            return optimisitc_max_geodes

        # Subproblems if we try to build one of the robots:
        can_build_count = 0
        for robot_index, costs in enumerate(self._costs):
            if not can_build_now(state, costs):
                continue
            can_build_count += 1
            if robot_index < 3:  # ore/clay/obsidian
                robots_count = state[robot_index]
                if robots_count >= self._max_costs[robot_index]:
                    # there is no point in building given robot
                    continue
            new_robots = [state[i] + 1 if i == robot_index else state[i] for i in range(4)]
            new_state = State(
                ore_robots=new_robots[0],
                clay_robots=new_robots[1],
                obsidian_robots=new_robots[2],
                geode_robots=new_robots[3],
                ore=self._new_resource_count("ore", state, costs["ore"]),
                clay=self._new_resource_count("clay", state, costs["clay"]),
                obsidian=self._new_resource_count("obsidian", state, costs["obsidian"]),
                time_left=state.time_left-1,
            )
            geodes = max(geodes, state.geode_robots + self._max_geodes(new_state, max_so_far_by_time_left, stats))

        # Subproblem if we do not build new robots. There is no point in exploring it if we can
        # build all the robots (there is no profit from not building any robot).
        if can_build_count < 4:
            new_state = State(
                ore_robots=state.ore_robots,
                clay_robots=state.clay_robots,
                obsidian_robots=state.obsidian_robots,
                geode_robots=state.geode_robots,
                ore=self._new_resource_count("ore", state, 0),
                clay=self._new_resource_count("clay", state, 0),
                obsidian=self._new_resource_count("obsidian", state, 0),
                time_left=state.time_left-1,
            )
            geodes = max(geodes, state.geode_robots + self._max_geodes(new_state, max_so_far_by_time_left, stats))

        self._store[state] = geodes
        stats["calculations"] += 1
        return geodes
    
    def _new_resource_count(self, resource: str, state: State, current_turn_cost: int) -> int:
        robot_index = RobotIndexByResource[resource]
        robots_count = state[robot_index]
        resource_count = getattr(state, resource)
        max_cost = self._max_costs[robot_index]
        if robots_count >= max_cost and resource_count >= max_cost:
            return max_cost  # we can treat resource as if it was infinite
        return resource_count + robots_count - current_turn_cost
    
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
    with open("data_small.txt", "r") as f:
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
    # result = 1
    # for bp in blueprints[:3]:
    #     result *= bp.count_max_geodes(32)
    # print("part2", result)


if __name__ == "__main__":
    main()

