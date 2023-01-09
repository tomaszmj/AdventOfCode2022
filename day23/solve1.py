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
    for round in range(10):
        move_src_dst = {}
        move_dst_count = defaultdict(lambda: 0)
        for x, y in elves:
            if not has_any_neighbour(x, y, elves):
                continue
            for i in range(4):
                dir = DIRECTIONS[(round+i) % 4]
                if can_move(x, y, elves, dir):
                    new_pos = (x + dir[1][0], y + dir[1][1])
                    move_src_dst[(x, y)] = new_pos
                    move_dst_count[new_pos] += 1
                    break
        for src, dst in move_src_dst.items():
            if move_dst_count[dst] > 1:
                continue
            elves.remove(src)
            elves.add(dst)
    min_x = min(e[0] for e in elves)
    min_y = min(e[1] for e in elves)
    max_x = max(e[0] for e in elves)
    max_y = max(e[1] for e in elves)
    # for y in range(min_y, max_y+1):
    #     for x in range(min_x, max_x+1):
    #         if (x, y) in elves:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print("")
    result = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)
    print(result)

if __name__ == "__main__":
    main()

