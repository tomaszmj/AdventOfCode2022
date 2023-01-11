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


def find_path(
    board: List[str],
    blizzard_fields_by_time: List[Set[Tuple[int, int]]],
    time_begin: int,
    reverse: bool,
) -> int:
    print(f"running find_path with time_begin {time_begin}, reverse {reverse}")
    height = len(board)
    width = len(board[0])
    begin = (1, 0)
    end = (width - 2, height -1)
    # We are going to try to go in one of 4 directions or wait (0, 0).
    # We first try to go "in a greedy way" in the direction of destination
    # (the last subproblem checked will be explored first because
    # to_visit is a stack). Thanks to it, we are more likely to find
    # a good solution (not necessarily the optimal one) quicky.
    # It will help pruning suboptimal paths quicker (tests have shown
    # that the order of directions to check has huge impact on performance).
    directions_to_check = [(-1, 0), (0, -1), (0, 0), (1, 0), (0, 1)]
    if reverse:
        begin, end = end, begin
        directions_to_check = [(1, 0), (0, 1), (0, 0), (-1, 0), (0, -1)]
    initial_board_state = (begin[0], begin[1], time_begin % len(blizzard_fields_by_time))  # (x, y, number determining state of blizzards)
    seen_states_with_min_time = {initial_board_state: time_begin}
    best_time = 1<<63
    stats = defaultdict(lambda: 0)
    to_visit = [(begin[0], begin[1], time_begin)]  # (x, y, time)
    try:
        while to_visit:
            stats["iterations"] += 1
            x, y, t = to_visit.pop()
            if (x, y) in blizzard_fields_by_time[t % len(blizzard_fields_by_time)]:
                stats["blizzard"] += 1
                continue
            min_time_left = end[1] - y + end[0] - x  # lower limit of time when we can reach the destination
            if min_time_left + t >= best_time:  # prune current path if there is no point in exloring it
                stats["min_time_left prune"] += 1
                continue
            for dx, dy in directions_to_check:
                nx = x + dx
                ny = y + dy
                if (nx, ny) == end:  # destination reached in the next move
                    best_time = min(best_time, t + 1)
                    stats["destination reached"] += 1
                    continue
                if (nx, ny) != begin and (nx <= 0 or ny <= 0 or nx >= width - 1 or ny >= height - 1):
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
        print(f"\nfind_path interrupted, current best_time: {best_time}, stats: {stats_str}\n")
        raise
    stats_str = ", ".join(f"{key}: {value}" for key, value in stats.items())
    print(f"find_path done - best_time: {best_time}, stats: {stats_str}")
    return best_time


def main():
    board = []
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                board.append(line)
    blizzard_fields_by_time = precompute_blizzards(board)
    time1 = find_path(board, blizzard_fields_by_time, 0, False)
    print("part1:", time1)
    # For part2 we can divide whole path into 3 parts in a "greedy" way.
    # There is no point in checking suboptimal partial paths, because
    # even if there was a solution that takes longer path from begin to end
    # to avoid blizzards on path from end to begin, we can reach the same
    # goal by waiting: go begin->end in the fastest way possible and
    # wait in end position for blizzards to pass (step with dx, dy (0, 0)).
    time2 = find_path(board, blizzard_fields_by_time, time1, True)
    time3 = find_path(board, blizzard_fields_by_time, time2, False)
    print("part2:", time3)


if __name__ == "__main__":
    main()

