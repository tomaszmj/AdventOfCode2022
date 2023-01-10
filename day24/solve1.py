#!/usr/bin/python
from typing import List, Set, Tuple, Dict

# precompute_blizzards returns a list - each i-th element of that
# list is a set of fields occupied by blizzards in minute i.
# It can be precomputed because blizzards move periodically.
# Each blizzard's period is equal internal board
# width (for ">" and "<" blizzards) or height (for "^" and "v" blizzards).
# Whole board's period (state of blizzards) must be no longer than internal board width*height
# (to be more precise - least common divisor of width and hight, but that's just a detail).
def precompute_blizzards(board: List[str]) -> List[Set[Tuple[int, int]]]:
    blizzard_types = {
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
        "^": (0, -1),
    }
    blizzards: List[List[int, int, int, int]] = []  # [current x, current y, direction x, direction y]
    blizzards_starting_direction_by_field = {}  # this is just to detect period in blizzards' positions
    for y, line in enumerate(board):
        for x, c in enumerate(line):
            if c in blizzard_types:
                direction = blizzard_types[c]
                blizzards.append([x, y, direction[0], direction[1]])
                blizzards_starting_direction_by_field[(x, y)] = direction
    height = len(board)
    width = len(board[0])
    max_period = (width-2) * (height-2)  # -2 because of "walls" surrounding the board
    print(f"precompute_blizzards called with width {width}, height {height}, max_period {max_period}")
    fields = set()
    for b in blizzards:
        fields.add((b[0], b[1]))
    occupied_fields_by_time = []
    periodic = False
    while not periodic:
        occupied_fields_by_time.append(frozenset(fields))
        fields = set()
        blizzards_direction_by_field = {}
        for b in blizzards:
            dx, dy = b[2], b[3]
            x = b[0] + dx 
            y = b[1] + dy
            if x == width - 1:
                x = 1
            elif x == 0:
                x = width - 2
            if y == height - 1:
                y = 1
            elif y == 0:
                y = height - 2
            b[0] = x
            b[1] = y
            fields.add((x, y))
            blizzards_direction_by_field[(x, y)] = (dx, dy)
        if blizzards_direction_by_field == blizzards_starting_direction_by_field:
            periodic = True
        if len(occupied_fields_by_time) > max_period:
            raise BaseException(f"periodic positions of blizzards not detected after {max_period}")
    print(f"blizzards started to be periodic after {len(occupied_fields_by_time)}")
    return occupied_fields_by_time


def main():
    board = []
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                board.append(line)
    dst_y = len(board) - 1
    dst_x = len(board[-1]) - 2
    occupied_fields_by_time = precompute_blizzards(board)
    to_visit = [(1, 0, 0)]  # (x, y, time)
    visited = {(1, 0, 0)}
    while to_visit:
        x, y, t = to_visit.pop()


if __name__ == "__main__":
    main()

