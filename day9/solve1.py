#!/usr/bin/python

directions = {
    "R": (1, 0),
    "D": (0, -1),
    "U": (0, 1),
    "L": (-1, 0),
}

def main():
    visited_points = {(0, 0)}
    head = [0, 0]
    tail = [0, 0]
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                direction = directions[line[0]]
                count = int(line[2:])
                for _ in range(count):
                    head[0] += direction[0]
                    head[1] += direction[1]
                    dx = head[0] - tail[0]
                    dy = head[1] - tail[1]
                    abs_dx = abs(dx)
                    abs_dy = abs(dy)
                    if abs_dx > 1 or abs_dy > 1:
                        tail_move_x = 0 if dx == 0 else dx // abs_dx
                        tail_move_y = 0 if dy == 0 else dy // abs_dy
                        #new_tail = [tail[0] + tail_move_x, tail[1] + tail_move_y]
                        #print(f"head {head}, tail moves from {tail} to {new_tail}")
                        tail[0] += tail_move_x
                        tail[1] += tail_move_y
                        visited_points.add((tail[0], tail[1]))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
    print(len(visited_points))


if __name__ == "__main__":
    main()

