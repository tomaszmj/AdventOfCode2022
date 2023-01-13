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


def chamber_rows_eqal(chamber: Set[Tuple[int, int]], row0: int, row1: int) -> bool:
    any_element_in_chamber = False
    all_eqal = True
    for x in range(7):
        ok0 = (x, row0) in chamber
        ok1 = (x, row1) in chamber
        any_element_in_chamber = any_element_in_chamber or ok0 or ok1
        all_eqal = all_eqal and (ok0 == ok1)
        if not all_eqal and any_element_in_chamber:
            return False  # quick return
    if not any_element_in_chamber:
        raise BaseException(f"chamber_rows_eqal(chamber, {row0}, {row1} does not make sense - all coordinates are out of chamber")
    return all_eqal


def check_chamber_cycle(chamber: Set[Tuple[int, int]]):
    end = max(c[1] for c in chamber) + 1
    max_h, y0_at_max_h, y1_at_max_h = 0, 0, 1
    for y0 in range(end-1):
        for y1 in range(y0+1+max_h, end-max_h):
            h = 0
            max_current_h = min(y1 - y0 - 1, end - y1 - 1)
            while h <= max_current_h and chamber_rows_eqal(chamber, y0+h, y1+h):
                h += 1
            if h > max_h:
                max_h = h
                y0_at_max_h = y0
                y1_at_max_h = y1
    print(f"detected chamber shape similarity at y0={y0_at_max_h}, y1={y1_at_max_h}, h={max_h}, chamber height {end}")


def check_height_cycle(delta_height: List[int]):
    end = len(delta_height)
    max_len, max_i0, max_i1 = 0, 0, 1
    for i0 in range(end - 1):
        for i1 in range(i0+1+max_len, end-max_len):
            ll = 0
            max_ll = min(i1 - i0 - 1, end - i1 - 1)
            while ll <= max_ll and delta_height[i0+ll] == delta_height[i1+ll]:
                ll += 1
            if ll > max_len:
                max_len = ll
                max_i0 = i0
                max_i1 = i1
    if max_i0 + max_len == max_i1:
        print(f"detected height diff similarity at i0={max_i0}, i1={max_i1}, max_len={max_len}, rocks fallen {end}")
    else:
        print(f"detected pseudo-height diff similarity at i0={max_i0}, i1={max_i1}, max_len={max_len}, rocks fallen {end}")


def main():
    height = 0
    chamber: Set[Tuple[int, int]] = set()
    moves = itertools.cycle(INPUT_SMALL)
    rocks_as_sets: List[Set[Tuple[int, int]]] = []
    for rock in ROCKS:
        rock_set = set()
        for rock_y, row in enumerate(rock):
            for rock_x, r in enumerate(row):
                if r == "#":
                    rock_set.add((rock_x, len(rock)-rock_y)) 
        rocks_as_sets.append(rock_set)
    rocks = itertools.cycle(rocks_as_sets)
    delta_height = []
    last_height = 0
    for _ in range(len(ROCKS)*len(INPUT_SMALL)*3+15):
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
        delta_height.append(height - last_height)
        last_height = height
    check_chamber_cycle(chamber)
    check_height_cycle(delta_height)


if __name__ == "__main__":
    main()

