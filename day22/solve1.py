#!/usr/bin/python
from typing import List


def all_ints_from_str(s: str) -> List[int]:
    numbers = []
    number_begin = -1
    for i, c in enumerate(s):
        isnumeric = c.isdigit() or (c == "-" and i < len(s) - 1 and s[i+1].isdigit())
        if isnumeric and number_begin == -1:
            number_begin = i
        elif not isnumeric and number_begin >= 0:
            numbers.append(int(s[number_begin:i]))
            number_begin = -1
    if number_begin >= 0:
        numbers.append(int(s[number_begin:len(s)]))
    return numbers


ROTATIONS = [
    (1, 0),  # >
    (0, 1),  # v
    (-1, 0), # <
    (0, -1),  # ^
]
ROTATION_ARROW = ">v<^"


def rotate(direction: str, rot: int) -> int:
    if direction == "L":
        return (rot - 1) % len(ROTATIONS)
    if direction == "R":
        return (rot + 1) % len(ROTATIONS)
    raise BaseException(f"unexpected rotation {direction}")


def main():
    board = []
    moves = []
    rotations = []
    width = 0
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.rstrip("\n")
                if not line:
                    continue
                if line[0].isdigit():
                    moves = all_ints_from_str(line)
                    rotations = "".join(c for c in line if c in "LR")
                else:
                    width = max(width, len(line))
                    board.append(line)
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    for i, b in enumerate(board):
        if len(b) < width:
            board[i] = b + " " * (width - len(b))
    height = len(board)
    y = 0
    x = board[0].index(".")
    rot = 0
    # board_as_list = []  # modifiable version of board to record moves, just for visualisation
    # for bb in board:
    #     board_as_list.append(list(bb))
    # board_as_list[y][x] = ROTATION_ARROW[rot]
    for i, steps in enumerate(moves):
        dx, dy = ROTATIONS[rot]
        for _ in range(steps):
            nx = (x + dx) % width
            ny = (y + dy) % height
            while board[ny][nx] == " ":
                nx = (nx + dx) % width
                ny = (ny + dy) % height
            if board[ny][nx] == "#":
                break
            if board[ny][nx] != ".":
                raise BaseException(f"unexpected board[{ny}][{nx}] = '{board[ny][nx]}'")
            x = nx
            y = ny
        if i < len(rotations):
            rot = rotate(rotations[i], rot)
        # board_as_list[y][x] = ROTATION_ARROW[rot]
    # board_as_list[y][x] = "X"
    # print("\n".join("".join(b) for b in board_as_list))
    print(1000*(y+1) + 4*(x+1) + rot)


if __name__ == "__main__":
    main()

