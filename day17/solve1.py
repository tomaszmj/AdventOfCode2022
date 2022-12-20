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

INPUT_SMALL = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

INPUT = "><<>>>><>>><<>><<>><<<<>>><<<<>><<<>>>><<>><><<<><<<>><>>>><<<>><<<<><<><<<>>><>><<<<>><>>><<<<>>>><<>>>><<<>><><<<<><<>>><>>>><>>><>>>><<<<><<>>><<>>><<<<>>>><<<><>><<>><<<<>>><<<>>>><>><>>>><>>><<<<><<>><>>>><<<<><<>>>><<>>><>><<<>><<<<>>>><<<>>>><<<>>>><<<<>>><<<<>>><>><<>>>><<><<<<>><<>><<>>><<<>>>><>><<>>>><<>><<<<>>>><<>>>><>><>>><<<<><<>><<>>>><<><<<>>>><>>><<<<>>><<<>><<<><>>>><<<<><<<<>>><<<<><<<>><>><<<<>>>><<>>><<>><<>><<<><<<<><<<>>>><<<><<<<><<<<>><<<<>>><>>><<<<>>><<<><<<><>><<<<>><<<><<<<>>>><<>><<>>><<<<>>>><<><<<<>>>><<>>>><<<>>><<>><<><<<><<<<>>><<<<><><>>><<<<>>><<<>>><>>>><<<>>>><>>>><<<<>>><<<>><<>><<><<<<>>>><<<><<<<><<<<>><<<<>>>><>>>><<>>><<<<>><<<>>>><<><><<<<>>><>>>><<<>>><<<>>><>>>><>><<>>><>><<<><<<>>>><<<<>>>><><<>>><>><<<>>><<<>>><<<<>>>><<<<>>>><<>>><<<><<>><<<<><<<<>>>><><<>>>><<>>><<>>>><<<>>><<>><<>>><>>>><<<<>>>><<>>>><<>>>><<>>><<<>>><<<>>>><><<<<>>><>>>><<<>><<<>>>><<>>>><<<<>>><>>>><<<>>>><<>><>>>><<<>><<<><<<>>>><><<>>><<><<>>><<>>>><<>>>><<<>>><<<>><<><>><<<<>>><<<><<>>>><<<>>><<><<<<><<><<<<>>>><<<<>>>><<<><>>><>>><<<<><<<<><>><<<<>>>><<>>><>>><<<<>><><<<>>>><>>><<<>><>>>><<<<>>><<<>>>><<>><>><<<>><<<<>>>><<<<>>><<<<><<>>>><<>><<<>><<<>><<<><<><<<<>><<>>><<>><<<>>><<<<>><>>><<<>>>><<<<><<>>><<<<>><<<>>>><<<><<<><<>>><<>>>><<<<>>>><<<><<<>>>><<<<>>>><<<>><>>><<>>>><><<<<><<<<>><<><>>><>><<>>>><<<<><><<<<>>><<<>>>><<<>><<<>>><<<>>><<>><>>><<<><><>>>><>><>><<<>><<<<>><<<>>>><<<<>>><<<<>><>>>><>>>><<<>><>><<>>><<<<>><>>><<<>><>><<>>>><<<<>>><<>>>><<<><<>><<>>>><>><>>><<><>><<>>>><<<>><><<>>>><<<>>><<>><<<>>><>>>><>><<>><>><<<<>>><>>><<>><<>>>><<<><<<<><<>>>><<>><<>>><>>><<<>>><<>>>><<<<><<><><<<<>>>><<<<>>><<<><>>><<<<>>>><<<>><>>><<<>><<<>>>><<>><<<><<><<<<><><>>>><<>><>>>><>>>><<<<>>><<>><<<<>><<>>><<<>><<<<><<<>>><<<>>>><<><<><<<<>><>>><<><<<<>><<><><>><<<><<<<>><<<><<>><<>><>>><>>><<<<>>>><>>>><<<<><>><<<<>>>><<<<>>><<<<>>>><<<>>><<>><>><>>><<>><<<>>><<<>>><<<<>>>><<<<>>><<<>>>><>>>><><><<>>>><<>>>><<<<>>><<<<>>>><<>>><>><<<<>>><<<<>>>><<<><<<<>>>><<>>><<<><>><<>>>><<<>>><<<>>><>>><<<>>>><<<<>>>><<<><<>><<<><>>>><<>>><<>>>><>>><<>><<<>>>><<<<>>>><<<<>>><>>>><><<<<>><><<><><<<<><<<<>>>><><<><<<<>><<<<><<<<>>>><<<>>><<<<>>><>>><<>>><<<>><<<<>><>>><<<<><>><<<<>>>><>>>><<>>><>><>>><>>>><>><<<<>>><<<>><<<>>><<>>><<<>>>><<><<<<>>>><<<<>>><<<<>><<<<>>>><>>>><<<<>>>><<<>>>><><<<<>>>><<>><<<>><<<>>>><<>>><<<<>>><>>>><<<>><>>>><<>>>><<>>>><<><><<><<>><<<<>>><<<<>><<<>><>>><>>>><<<>>>><<>><><<<><<<<>>>><<><<<<><<<>>><<<><>>>><<>>>><<<<>><<<>><><<<>><<<<><<<>>>><<><><<<<>>><><>>>><>>>><<<<>><<><>>><<>>>><<>>><>>><<>><<<>><><><><>><<>>><>><<<>>>><<<>><>>><>>>><>><<>>><<>>>><<<<>>><<>><<<<>>><>><<<<>>><>>>><><<<>><<<>>><<<<>>><<><<<><<<<>>><>>><><<<<><<<>>><<>><><<<<>><<<><><<<<>>>><<<><><<>>><<<>><>>><<>><<<<><>><<><<<<>><<<>><>>><>>>><<<><<<>><<>><<<<>>>><<>><>>><>>><<<<>>><>>>><<<<>>>><<>>><<>>>><<<<><<<><<<>><<<<>><<<>>><<<<>>>><<<>>>><<>>>><<<<><<<<>>><<<<>><<><<<<><>><<<>><<<<><<>>>><<<><<<<>><<<<><><<<>>><>>>><<<<>>><<<<>><>><<<<><<<><<<>>><<<><<>>><<<><<<>>>><<<>>><<<><<<><<><<<>>><<<<>><>>>><<<<>>><<<>>><<<<><<>>><<<<>>><<<<>><>>><<><<<><<<<><<>><<<>>><<><<<>><<<<>><<>>><<<<><<<>>>><>>><<<<><>>>><<<<><<<<>><<>>><<><<<<>><<><>>><<<<>>><<<>><<<>>>><>><<>>><>>>><>>>><<<<>><<><<<>>>><<>><<<<>>><<>>><<>><<>><>>>><<><<<<>>><>>>><<>>>><<>><>>><<<<>>>><<<><>>><<>>><>>>><<<<><<>><<<>>>><<>><<<<>><<<><<>>>><>>>><<<<><><<<><<<<>><<<>>>><>>>><<<><><<<><<<>>><>>><<<>><<<>>>><<<><<<>>><<<<>>><<>>><<<>><>><>><<>>>><>><<<>>><<<><<<<>>><<<>>>><<>>><>><<>>>><<>>>><<>>><<><<>><<>>><<<<>>><<<<>><<<<>>>><<<>>>><<<<>><<>><<<<>><<<>>>><<>>>><>>><<<>><>>><>><<<><<<><<>>>><<<<>><><>><<<<>>>><<>>>><<>>>><<<>>><<<>>><<<<>>>><>>>><><<><<>>>><<>>>><>><<>><>><<>><<>><<<>>>><<>><<><<><<><<<<>>><<<<><><>>><<<>><><<<><<<<>><<>>>><<>><<<<>><<>><<>>><<><<>>>><>><<<<>>><><<>><>>>><<<<>>><<>>>><<><<<>>>><><<<>><>><<>><<><<<<>>><<><><<<<>>>><>>><><<>>>><<>>><>>>><<<<>>>><<>><<<>><<<>>>><>>>><<<><>><<>><<<<>>>><<<>>>><<<>>>><<<>><<<<>><<<<><<<<>>>><<>><<<<><<>><<<>>><<>>>><<<<>>>><>>>><<>>>><<<<>>><<<<>><<<>><<>>>><>><<>><<>><<>><<<<>>>><<<><<>>><<<><<<<>><<>><<<<>>><<<<>>><<<><>>>><<<<>>><<<<>>><>><<>>>><<<<><<<<>>>><<<<><<>>><<<<><<><<<>>><>><<<<>>>><<<><<<>>>><>>>><<<>><><<<<><<<>>><<>>><<<<>><<<<>>><<>>><<>>><<<<><<<>><>>>><>><<<<>>><>>><<>>><<>>><<><<>>>><<<>>>><<<>>><>>><<<>><>>>><<<>>><><<>>>><<<<>>><>>><<<<>>>><<<>><<<><<>>><<<>>><<<<>><<<<>><>><<<>><<<<>>>><<><>><>>>><<<<>>><>>><<<<>>><>>><>>><<<>>><<<><<<>><>><<<><<>>><>>><<<<>>><<<<>>><<>>>><>>><<<>>>><<<<><<>><<><><<<><<>><>><<<>>><<<<>>><>>><<<>>>><<<<>>>><<<>>><><<<<>>><<>>><<>>>><<>><<<<><>>><<<>>>><<><<><<>>><<><<<><<<>>>><>>><><><>>>><<>>><><<<>><><<>><><>><>>><><<<><<><>>><<<<>><<<<>>><>>><<>><<>>>><<<<><<<><<<<>>><<<<>><<<<>>><<>><<<>><<>><<>>>><<<<>>>><<>><<<><>><<<<>>>><<>><<><<<>><<>><>><<<>><<<>><<<>>>><<>>><<>><<<>><<>>><><>><<>>><>>><<<<>>><<<<>><<><>>><><<>>>><<><><<<>><>><<>>>><<<>>>><<<>><>>>><<<<>><<>>>><>>>><<<>><<>><>>><<<<><><><<<>>>><>>>><<><<<><><<<>>>><<<<>>>><><><<<>>><<<>><<<>>><<<<>>>><<<<>>><<>><><<<>>>><<>>><>>>><<<<>>><>>>><<<><<<>><<<>><<<><<<><<<>>>><<<<>>><<>>><>>><<>><>>>><<>>>><<>>>><<<>>>><<<>>><>>><<<<><><<>>><<<<>>><>><<<<>><>><<<><><<<<><>>><<<>>>><>>>><>>>><<<><<<<><<<<>>><<<>><<<>>><<>>>><<>>>><<<<>><<<>>><<<>>>><<<<><<>>>><<>><<<>><<<<><<><><<><>>><><<<><<<<>>><>>>><<><<<<>>>><>>>><>>><<>>><<<<>>><><<<<>>>><>>><<>><<<>>>><<>>>><<<>>>><<><<>>>><>><<<<><<><<<<>><<<><<<>>>><><>>><<>>>><<>><>><<<<>><<<>>>><>><<<>><<<>><<<><<<>><<<>><><<<<>>>><<>>><<<>>><<>>><>>>><>>>><<><<<>>>><<>>><>><<<<>><<><<<>>>><<>>>><>><<<<>>><<<<>>>><<<<><<<<>><<>>><>>><<<<>>>><<<>>><>><<<<>>><><<<<><<>>><<>>><><<<><<<<>><>>><<<<><<<><<><<<<><<<<>><<<<><<<<>>>><<<<>><>>>><>>><<<<><<>><>><<>>>><<<<>><<<<>>><>>><<<>>><<<>>><<<<>>><>>><<<<>>>><<<><<<><<<><<><<<>><<<>><<<>>><>><<>>><<>><<<<>>><<<<>><<<<><>>>><>>>><<<>>><<<>>><<><<<>>>><<<><<>><<>>><<><<<<><<<<>><<<>><>>><<<<>><<><<<<>>><<>><<<><>><<<<>><<<>><<>>><<<<><<>>>><<><<>>>><<<<>>>><<<><<<><<<<>>>><<<<><<>>>><<>>>><>>><<<>>>><<<<>>>><>>>><>>>><<<<><<><>><<><<>>>><>>>><><<<<>><<<<>><<>>><<>><>>>><<><<><<>><<<<>>><<<<>>>><<>><<>><<><><>><<<>>>><<<><<<>><<<<><<<<>>>><<<<>>>><<<>>><<><<>>>><<<><><<>>>><<<><<<><<<<>><>>>><<><<<><>>>><<>>>><<<<>><<<>><<>><<>><<>>>><<>>><>>>><>>><<>>>><<<>><<<>><<>><<<><<>><<<<>><<>>>><<<>>>><<<>>>><<><<<<><<<>>>><>>><<<><<<>>><<<<>>>><<><<<<>><<<>>><>>>><<<>>><<<<>>><<<>>>><>>>><<<<><<>><<<<>><><<<>><<>><<<>><<>>>><>>>><><<<>>>><<>>><<<>>>><<<<>><<>>>><<><<<<>><<<<>>><><<>><<<><<<>>>><<<><<<<>>><>>>><<<>><<>>><<>><><<><<<<><>>><>>>><>><>><<<>>>><<<<><<<<>>>><>>><<><<<>><<<>><>><>>>><><<>>>><>>><<<<><<<><>><><>>><<<><<<><<<<>>><<<>>><<<>><<<>>>><<<>>>><<<>>>><<<>>>><<<<>>><<<<><>>><><<<>>>><>>><<>><>><<<>>>><<<<><<>>>><>>><>>><<<>><<<<>>><<<><>>><>>><<><<><<<>>><<<<>>>><<<<>>>><>><<<<><<>>><<<<>>>><<>>><<<<><>><<>>><><<<<>>>><>>><<<<><<<<>>><<<<><<>>>><<<<>>>><<<<>>><<<>><>>><>>><<<<>>><>><<>><<><<<>>><<<><<<<>>>><>>>><<<<><<<<><<>>><<<>><>>><<<<>>>><<<><<<>><<>>>><><><<<<>><<<<><<<<><<<>>><<<>>><>><<<<>><<<<>><<<>>>><>><<>><<<<>>>><<<<>>>><<<>>><<<<>>><<<<>>><<<><<<<>>>><<>>>><<>>><<<>>>><><<<<><<<<><<>><>>>><>>><<<>><>>><<<<><<<<><<>>><>>><><<<><<>><<>>><<>>>><<<><>>>><<<>><<<><<>><<>>><<<<>>><<><<><><>>><><<>>><<<<><<<>>>><<<>>>><>>><<>>>><<<><<<>><<<>><<<<>>><<><<><<<<>>>><<>>>><>>><<>>>><><<<<>>><<<<>><<><<>>>><<<<>><<<<>>><<<<>>>><<<>>>><>>>><<<<>>>><>><<>>><<<><>>>><<>>>><<<>>><<>>>><<<>><<<>>>><<>><<<>>><<>><<><>><<><<<>>><<<>>><<<<>><<>>><>>>><<<<><<<><><>>><<<>><<<<>>><<>>>><>><>>>><<<<>>>><>>>><<<><<>>>><<<<><<<>>>><<<><><<<<>><<>>>><>>><<><>>><<>>>><>>><<>>><><<>>>><<<<>><>>><<<><<>><<<<>>><<<>><<<<>>><<>>><>><<<>><>>><<<<>>>><<<>><<>>><<<<><<>>>><<<<>>>><<><><<<<><<<>>>><<>>><<<<>>><<>>><<<<>><<<<><<>>>><<><>>><<<>><<<><<<>>><<<<>><<><>>>><<<><>><<>><>>>><<<<>><<<<>><><<<<><<<>>><<<<>><><>><<<<>>><>>>><<<<>>>><><<<<>>><<<<>>><<<<><><<<<>>>><<<>>>><<<<>><<>>><<<<>><<<><<>><><<<><<<>>><<<<>>>><<>>>><<>><<>>>><<<<>>><>><<><<>><<>><<<<><<<<>><<<>><<<>><<>>>><<<>>>><<<<>><>><>>>><<><<<<>><<<>><<<>><>>>><<<>>>><>>><<<<>>>><<<>>>><<><>>>><<<<><<>>>><<>>><<<<><<><<<<>>>><<>>><<><<<><<>><<<>><<>><<<><><<<<>>><<<<><<><<>><<>>><<<<>>><>>>><>>>><>>><><<<>><><<<>>>><<>>><<<<><<<><<<<><<<>>>><<>><>>><<<>>><>>><<>>>><>>>><>>>><<<>>>><>><<<><>><<<>>>><<>>><<>><>>>><>><<<<>>><<>><<><>>><><<<<>>>><<<><<<<>>><>>>><<><<<>>>><>>><<<<>><<>><<>>><>><>>><<<>>><>>>><<<><<<>>>><<<<>><<<>>><<<>>>><><<>><<><<<>>><><<<<><>>>><<<<>>><<><>>>><><<<<>>>><<<<>>>><><<><<>>><>><<<<>>><<<<><>>>><<>><<<<>>><>><<><<><<<>>>><<<<>><<<<>>>><>><<<<>>>><<<>>><<>>><><<<<><<<<>>><<>>><<<>>>><<<>>><><>><>>>><<<<><<>><<<<>>>><<<<>>>><<<<><<<><><>><><<<>>>><<<<>><<>><>>><<<>>><>>><<><<><>><>><<<>>>><<<<>>><><<<<><<<>>><<><<<>>><<<<><<<>>><<<>>>><<>>>><<>><>>><><<><<<>><>><<<<>><<>><>><<<<><<<<><>>>><<<<>>><<<><<<>><<><<<<>>><<<>>><>><><>>>><<<><>><<<<><>><<<<>>><><<><>><><<<<>>>><<><<<>>><<>>>><<<<>><<<>>><>>>><<>><>><<<<>>><<<>><><><>>>><<<>><<<<><<<>><<<<>><<<>>>><<>>><<<<>><><<>><<<>><<<<>>><<<>><>>>><<><<><>>>><<<><<>>>><><<<>><<>>><>><<<<>>><<<<><<<>>><<<<>>>><<>>>><<<>><<>><<<<>>><<<<>><>><<<>><<>>>><><<<>>>><<<>><>>>><<<>>>><<<<><<>><<<<>>><<>><><<>>><<<>><<>><<<>><<>>><<>>><<<>><<<>>><<>><<>><<<<>>>><<<<>>>><<<<><<>><<<>>><<<>>>><<<>><>>><><>><>>><><<>>>><>>><<<<>>>><<<>>>><>>><<<><<<>>><<<>><>>>><<<<>>><<<<><<<>>><<>>><<<>><<<<>><<<><<<>>>><><<<<>><<<<>>>><<<><<<>>><<<><<<<><>><>><<>>><<<>>><>>><><<<><<>>>><<<>>><>>><>>><>>>><<<><<<<>>>><<><<>><<<><<<><<<<><>><<><<<>>><<>>><<><<>>><<<<>><>><<<>>><<<<>>><>>><<<<>><>><<<<>><<>>>><<>>><>><<>><<<>><<<>>><<<<>><<<><<<>>>><<<>>><<>><<<<>><<<<>>><<<<>>>><<<>><<<<>>><>><<>>><<<>>><<<>>>><<<<>>>><<<><<<>>><<<>>><>>><>><<<<><><<<>><<<>>>><<<>>>><<<<>>>><<>><<>>><>><<<>>><<>><>><>><<<>>><>>><<<<>>><<<><<<>>><<<>><<<>><<<<>>><<<<>><<><><>>><<><<<<>>><<<<><<>><<<>><>><<<>>><<<>>>><<<<>>>><>>><<>>><<<<>><<<<>>>><<<>><<<>>><<<<><<<<><><<<>><>><<<<>><>>><<<><<<<>>><<<>><<<<><<<<>><>>><>><<><<>>>><<<<><<><<<<><<<<>>><<<><<<<>>><<<<><<<>>><<<"


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


def main():
    height = 0
    chamber: Set[Tuple[int, int]] = set()
    moves = itertools.cycle(INPUT)
    rocks_as_sets: List[Set[Tuple[int, int]]] = []
    for rock in ROCKS:
        rock_set = set()
        for rock_y, row in enumerate(rock):
            for rock_x, r in enumerate(row):
                if r == "#":
                    rock_set.add((rock_x, len(rock)-rock_y)) 
        rocks_as_sets.append(rock_set)
    rocks = itertools.cycle(rocks_as_sets)
    for _ in range(2022):
        rock = rocks.__next__()
        x, y = 2, height + 3
        while True:
            c = moves.__next__()
            dx = 1 if c == ">" else -1
            if rock_can_move(chamber, rock, x, y, dx, 0):
                x += dx
            if rock_can_move(chamber, rock, x, y, 0, -1):
                y -= 1
            else:
                break
        for rx, ry in rock:
            height = max(height, y + ry)
            chamber.add((x + rx, y + ry))
    print(height)


if __name__ == "__main__":
    main()
