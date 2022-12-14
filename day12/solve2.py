#!/usr/bin/python
from collections import deque 
from typing import Tuple, List


def find_path(grid: List[List[int]], end: Tuple[int, int]) -> int:
    to_visit = deque([(end[0], end[1], 0)])  # (y, x, steps from start)
    visited = {end}
    # breadth first search, reversed from the end until height 0
    while len(to_visit) > 0:
        y, x, steps = to_visit.popleft()
        c = grid[y][x]
        if c == 0:
            return steps
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y1, x1 = y + d[0], x + d[1]
            if (y1, x1) in visited:
                continue
            if 0 <= y1 < len(grid) and 0 <= x1 < len(grid[0]):
                if c - grid[y1][x1] <= 1:
                    to_visit.append((y1, x1, steps+1))
                    visited.add((y1, x1))
    return -1


def main():
    grid = []
    end = None
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                line = line.replace("S", "a")
                if not end:
                    x = line.find("E")
                    if x >= 0:
                        end = (len(grid), x)
                        line = line.replace("E", "z")
                if len(grid) > 0:
                    if len(line) != len(grid[-1]):
                        raise BaseException(f"mismatching line lengths: {len(line)} != {len(grid[-1])}")
                grid.append(list(ord(c)-ord('a') for c in line))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    if not end:
        raise BaseException("cannot run search - missing end")
    print(find_path(grid, end))


if __name__ == "__main__":
    main()

