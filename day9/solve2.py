#!/usr/bin/python

directions = {
    "R": (1, 0),
    "D": (0, -1),
    "U": (0, 1),
    "L": (-1, 0),
}


def print_rope(rope: list):
    min_x = min(r[0] for r in rope)
    max_x = max(r[0] for r in rope)
    min_y = min(r[1] for r in rope)
    max_y = max(r[1] for r in rope)
    points = {(0,0): "s"}
    for i in range(len(rope)-1, 0, -1):
        points[(rope[i][0], rope[i][1])] = str(i)
    points[(rope[0][0], rope[0][1])] = "H"
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in points:
                print(points[(x, y)], end="")
            else:
                print("#", end="")
        print("")


def main():
    visited_points = {(0, 0)}
    rope = list([0, 0] for _ in range(10))
    #print_rope(rope)
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                direction = directions[line[0]]
                count = int(line[2:])
                for _ in range(count):
                    rope[0][0] += direction[0]
                    rope[0][1] += direction[1]
                    for i in range(1, len(rope)):
                        dx = rope[i-1][0] - rope[i][0]
                        dy = rope[i-1][1] - rope[i][1]
                        abs_dx = abs(dx)
                        abs_dy = abs(dy)
                        if abs_dx > 1 or abs_dy > 1:
                            move_x = 0 if dx == 0 else dx // abs_dx
                            move_y = 0 if dy == 0 else dy // abs_dy
                            rope[i][0] += move_x
                            rope[i][1] += move_y
                            if i == len(rope) - 1:
                                visited_points.add((rope[i][0], rope[i][1]))
                #input()
                #print_rope(rope)
                #print("\n")
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                if isinstance(e, KeyboardInterrupt):
                    raise
    print(len(visited_points))


if __name__ == "__main__":
    main()

