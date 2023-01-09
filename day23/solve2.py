#!/usr/bin/python
from collections import defaultdict

DIRECTIONS = [
    # each direction is a tuple of 3 neighbours to check (dx, dy),
    # middle one being the position to be moved to
    ((-1, -1), (0, -1), (1, -1)), # north
    ((-1, 1), (0, 1), (1, 1)), # south
    ((-1, -1), (-1, 0), (-1, 1)), # west
    ((1, -1), (1, 0), (1, 1)), # east
]

ALL_NEIGHBOURS = (
    (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
)


def has_any_neighbour(x, y, elves_set) -> bool:
    for dx, dy in ALL_NEIGHBOURS:
        if (x+dx, y+dy) in elves_set:
            return True
    return False


def can_move(x, y, elves_set, dir) -> bool:
    for dx, dy in dir:
        if (x+dx, y+dy) in elves_set:
            return False
    return True


def main():
    elves = set()
    y = 0
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if line:
                    for x, c in enumerate(line):
                        if c == "#":
                            elves.add((x,y))
                    y += 1
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    round = 0
    while True:
        move_src_dst = {}
        move_dst_src = {}
        for x, y in elves:
            if not has_any_neighbour(x, y, elves):
                continue
            for i in range(4):
                dir = DIRECTIONS[(round+i) % 4]
                if can_move(x, y, elves, dir):
                    new_pos = (x + dir[1][0], y + dir[1][1])
                    if new_pos in move_dst_src:
                        src = move_dst_src[new_pos]
                        del move_src_dst[src]
                        del move_dst_src[new_pos]
                    else:
                        move_src_dst[(x, y)] = new_pos
                        move_dst_src[new_pos] = (x, y)
                    break
        if len(move_src_dst) == 0:
            print(round+1)
            return
        for src, dst in move_src_dst.items():
            elves.remove(src)
            elves.add(dst)
        round += 1


if __name__ == "__main__":
    main()

