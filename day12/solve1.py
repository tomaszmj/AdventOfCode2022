#!/usr/bin/python
from collections import deque 
from typing import Tuple, List


def find_path(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    to_visit = deque([(start[0], start[1], 0)])  # (y, x, steps from start)
    visited = {start}
    # breadth first search:
    while len(to_visit) > 0:
        y, x, steps = to_visit.popleft()
        if (y, x) == end:
            return steps
        c = grid[y][x]
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y1, x1 = y + d[0], x + d[1]
            if (y1, x1) in visited:
                continue
            if 0 <= y1 < len(grid) and 0 <= x1 < len(grid[0]):
                if grid[y1][x1] - c <= 1:
                    to_visit.append((y1, x1, steps+1))
                    visited.add((y1, x1))
    return -1


def main():
    grid = []
    start = None
    end = None
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if not start:
                    x = line.find("S")
                    if x >= 0:
                        start = (len(grid), x)
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
    if not start or not end:
        raise BaseException("cannot run search - missing start or end")
    print(find_path(grid, start, end))


if __name__ == "__main__":
    main()

