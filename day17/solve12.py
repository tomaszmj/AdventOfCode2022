#!/usr/bin/python
import itertools
from typing import Set, Tuple, List

ROCKS = [
    ["####"],
    [ ".#.", "###", ".#."],
    ["..#", "..#", "###"],
    ["#", "#", "#", "#"],
    ["##", "##"],
]

def print_chamber(chamber: Set[Tuple[int, int]]):
    max_y = max(c[1] for c in chamber)
    for y in range(max_y, 0, -1):
        for x in range(7):
            if (x, y) in chamber:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def rock_can_move(
    chamber: Set[Tuple[int, int]],
    rock: Set[Tuple[int, int]],
    x: int, y: int,
    dx: int, dy: int,
) -> bool:
    for rx, ry in rock:
        new_x = rx + x + dx
        new_y = ry + y + dy
        if new_x < 0 or new_x > 6:
            return False
        if (new_x, new_y) in chamber:
            return False
        if new_y <= 0:
            return False
    return True


def compute_height(
    rocks_count: int,
    heights: List[int],
    rocks_fallen_until_cycle_begin: int,
    cycle_period: int,
) -> int:
    if rocks_count < len(heights):
        return heights[rocks_count]
    cycle_height = heights[-1] - heights[rocks_fallen_until_cycle_begin]
    offset = rocks_count - rocks_fallen_until_cycle_begin
    cycles = offset // cycle_period
    remainder = offset % cycle_period
    return cycle_height*cycles + heights[rocks_fallen_until_cycle_begin + remainder]


def main():
    height = 0
    chamber: Set[Tuple[int, int]] = set()
    rocks_as_sets: List[Set[Tuple[int, int]]] = []
    with open("data.txt", "r") as f:
        data = f.read().strip()
    winds = [1 if wind == ">" else -1 for wind in data]
    for rock in ROCKS:
        rock_set = set()
        for rock_y, row in enumerate(rock):
            for rock_x, r in enumerate(row):
                if r == "#":
                    rock_set.add((rock_x, len(rock)-rock_y)) 
        rocks_as_sets.append(rock_set)
    floor = [0]*7
    floor_distance_from_height = (0,)*7
    states_seen = {}  # key: rock index, wind index, floor_distance_from_height, value: rocks fallen so far
    wind_index = 0
    heights = [0]
    for i, rock in enumerate(itertools.cycle(rocks_as_sets)):
        x, y = 2, height + 3
        state = (i % len(rocks_as_sets), wind_index) + floor_distance_from_height
        if state in states_seen:
            rocks_fallen_until_cycle_begin = states_seen[state]
            cycle_period = i - rocks_fallen_until_cycle_begin
            print(f"cycle detected: begin {rocks_fallen_until_cycle_begin}, period {cycle_period}, state {state}")
            break
        states_seen[state] = i
        while True:
            dx = winds[wind_index]
            wind_index = (wind_index + 1) % len(winds)
            if rock_can_move(chamber, rock, x, y, dx, 0):
                x += dx
            if rock_can_move(chamber, rock, x, y, 0, -1):
                y -= 1
            else:
                break
        for rx, ry in rock:
            height = max(height, y + ry)
            chamber.add((x + rx, y + ry))
            floor[x + rx] = max(floor[x + rx], y + ry)
        floor_distance_from_height = tuple(height - f for f in floor)
        heights.append(height)
    print("part1", compute_height(2022, heights, rocks_fallen_until_cycle_begin, cycle_period))
    print("part2", compute_height(1000000000000, heights, rocks_fallen_until_cycle_begin, cycle_period))


if __name__ == "__main__":
    main()

