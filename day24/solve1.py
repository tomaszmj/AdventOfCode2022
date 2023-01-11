#!/usr/bin/python
from typing import List, Set, Tuple
from collections import defaultdict

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
    blizzard_fields_by_time = []
    periodic = False
    while not periodic:
        blizzard_fields_by_time.append(frozenset(fields))
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
        if len(blizzard_fields_by_time) > max_period:
            raise BaseException(f"periodic positions of blizzards not detected after {max_period}")
    print(f"blizzards started to be periodic after {len(blizzard_fields_by_time)}")
    return blizzard_fields_by_time


def main():
    board = []
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                board.append(line)
    height = len(board)
    width = len(board[0])
    dst_y = height - 1
    dst_x = width - 2
    try:
        blizzard_fields_by_time = precompute_blizzards(board)
        to_visit = [(1, 0, 0)]  # (x, y, time)
        seen_states_with_min_time = {(1, 0, 0): 0}  # (x, y, board state): time, board state being time % len(blizzard_fields_by_time)
        best_time = 1<<63
        stats = defaultdict(lambda: 0)
        while to_visit:
            stats["iterations"] += 1
            x, y, t = to_visit.pop()
            if (x, y) in blizzard_fields_by_time[t % len(blizzard_fields_by_time)]:
                stats["blizzard"] += 1
                continue
            min_time_left = dst_y - y + dst_x - x  # lower limit of time when we can reach the destination
            if min_time_left + t >= best_time:  # prune current path if there is no point in exloring it
                stats["min_time_left prune"] += 1
                continue
            # Below we try to go in one of 4 directions or wait (0, 0).
            # We first try going right / down, then wait, then up / down
            # (the last subproblem checked will be explored first because
            # to_visit is a stack). We first try to go in the directions
            # that bring us closer to the destination, so that we are more
            # likely to find a good solution (not necessarily the optimal) quicky.
            # It will help pruning suboptimal paths quicker (tests have shown
            # that the order of directions to check has huge impact on performance).
            for dx, dy in [(-1, 0), (0, -1), (0, 0), (1, 0), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if nx == dst_x and ny == dst_y:  # destination reached in the next move
                    best_time = min(best_time, t + 1)
                    stats["destination reached"] += 1
                    continue
                if nx <= 0 or ny <= 0 or nx >= width - 1 or ny >= height - 1:
                    stats["board edge"] += 1
                    continue
                new_board_state = (nx, ny, (t+1) % len(blizzard_fields_by_time))
                if new_board_state in seen_states_with_min_time and \
                    seen_states_with_min_time[new_board_state] <= t + 1:
                    stats["state already seen earlier"] += 1
                    continue
                seen_states_with_min_time[new_board_state] = t + 1
                to_visit.append((nx, ny, t+1))
    except KeyboardInterrupt:
        stats_str = ", ".join(f"{key}: {value}" for key, value in stats.items())
        print(f"KeyboardInterrupt, current best_time: {best_time}, stats: {stats_str}\n")
        raise
    stats_str = ", ".join(f"{key}: {value}" for key, value in stats.items())
    print("stats:", stats_str)
    print("best_time:", best_time)


if __name__ == "__main__":
    main()

