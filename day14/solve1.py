#!/usr/bin/python
from collections import defaultdict


def main():
    cave = defaultdict(lambda: ".")
    max_y = 0
    min_x = 500
    max_x = 500
    cave[(500, 0)] = "+"
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if not line:
                    continue
                point_pairs = line.split(" -> ")
                points = []
                for pp in point_pairs:
                    p = pp.split(",")
                    points.append((int(p[0]), int(p[1])))
                for p in points:
                    min_x = min(min_x, p[0])
                    max_x = max(max_x, p[0])
                    max_y = max(max_y, p[1])
                for p1, p2 in zip(points[:-1], points[1:]):
                    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
                    if (not dx and not dy) or (dx and dy):
                        raise BaseException(f"unexpected step between points {p1} and {p2}")
                    step_x = dx // abs(dx) if dx else 0
                    step_y = dy // abs(dy) if dy else 0
                    x, y = p1[0], p1[1]
                    cave[(x , y)] = "#"
                    while x != p2[0] or y != p2[1]:
                        x += step_x
                        y += step_y
                        cave[(x , y)] = "#"
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    # print("cave before:")
    # for y in range(0, max_y+1):
    #     print("".join(cave[(x, y)] for x in range(min_x, max_x+1)))
    x, y = 500, 0
    grains_of_sand = 0
    while y <= max_y:
        if cave[(x, y+1)] == ".":
            y = y + 1
        elif cave[(x-1, y+1)] == ".":
            x = x - 1
            y = y + 1
            min_x = min(min_x, x)
        elif cave[(x+1, y+1)] == ".":
            x = x + 1
            y = y + 1
            max_x = max(max_x, x)
        else:
            grains_of_sand += 1
            cave[(x, y)] = "o"
            if x == 500 and y == 0:
                print("unexpected situation - (500, 0) point blocked by sand")
                break
            x, y = 500, 0
    print("cave after:")
    for y in range(0, max_y+1):
        print("".join(cave[(x, y)] for x in range(min_x, max_x+1)))
    print(grains_of_sand)


if __name__ == "__main__":
    main()

