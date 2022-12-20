#!/usr/bin/python
from typing import List, Tuple


def is_witin_bounds(p: Tuple[int], min_cube_coord: List[int], max_cube_coord: List[int]):
    for i, min_coord in enumerate(min_cube_coord):
        if p[i] < min_coord:
            return False
    for i, max_coord in enumerate(max_cube_coord):
        if p[i] > max_coord:
            return False
    return True


def main():
    cubes = set()
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if not line:
                    continue
                cubes.add(tuple(int(l) for l in line.split(",")))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    
    # find min and max cube coords
    min_cube_coord = [-1, -1, -1]
    max_cube_coord = [-1, -1, -1]
    for cc in cubes:
        for i, c in enumerate(cc):
            if min_cube_coord[i] == -1 or c < min_cube_coord[i]:
                min_cube_coord[i] = c
            if max_cube_coord[i] == -1 or c > max_cube_coord[i]:
                max_cube_coord[i] = c
                
    # add 1 margin in both sides, so that we are sure that min/max coords are outside of all cubes
    for i in range(3):
        min_cube_coord[i] -= 1
    for i in range(3):
        max_cube_coord[i] += 1

    # "flood-fill" whole space outside of cubes:
    outsiders = set()
    visited = set()
    to_visit = []
    to_visit.append(tuple(m for m in max_cube_coord))
    while len(to_visit) > 0:
        p = to_visit.pop()
        if p in cubes:
            continue
        outsiders.add(p)
        for coord in range(3):
            for delta in [-1, 1]:
                neighbour = tuple(p[i] if i != coord else p[i] + delta for i in range(3))
                if neighbour in visited:
                    continue
                if not is_witin_bounds(neighbour, min_cube_coord, max_cube_coord):
                    continue
                visited.add(neighbour)
                to_visit.append(neighbour)

    # copied solution from part 1, but with check if neighbour is within "outsiders":
    result = 0
    for c in cubes:
        for coord in range(3):
            for delta in [-1, 1]:
                c2 = tuple(c[i] if i != coord else c[i] + delta for i in range(3))
                if c2 in outsiders:
                    result += 1
    print(result)


if __name__ == "__main__":
    main()

