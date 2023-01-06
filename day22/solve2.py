#!/usr/bin/python
from __future__ import annotations
from typing import List, Tuple


ROTATIONS = [
    (1, 0),  # >
    (0, 1),  # v
    (-1, 0), # <
    (0, -1),  # ^
]

# Coordinates mapping is not fully generic. It works on my input data in this shape:
#      ..........
#      ..........
#      ..........
#      ..........
#      ..........
#      ..........
#      .....
#      .....
#      .....
#      .....
#      .....
# ..........
# ..........
# ..........
# ..........
# ..........
# .....
# .....
# .....
# .....
# .....
#
# Walls are numbered this way (numbers chosen arbitrarily):
#       ----- -----
#       | 0 | | 1 |
#       ----- -----
#       -----
#       | 2 |
#       -----
# ----- -----
# | 4 | | 3 |
# ----- -----
# -----
# | 5 |
# -----
class CubicCoords:
    length = 50

    board_segment_to_wall = {
        (1, 0): 0,
        (2, 0): 1,
        (1, 1): 2,
        (1, 2): 3,
        (0, 2): 4,
        (0, 3): 5,
    }

    wall_to_board_segment = [
        (length, 0),
        (2*length, 0),
        (length, length),
        (length, 2*length),
        (0, 2*length),
        (0, 3*length),
    ]

    # walls_neighbourhood is a list, with following elements
    # marking i-it wall neighbours (i from 0 to 5).
    # In each list element there is a list of 4 elements -
    # neighbour in the following direction (dx, dy):
    # (1, 0), (0, 1), (-1, 0), (0, -1) (the same order as ROTATIONS).
    # Each list of lists element is a tuple:
    # new wall, new rotation, function mapping coordinates.
    # Wall sides are numbered as follows (number is correlated with (dx, dy) list above):
    # --- 3 ---
    # |       |
    # 2       0
    # |       |
    # --- 1 ---
    # For example, the first element of the first list is (1, 0, lambda x, y: (0, y)) ->
    # wall's 0 neighbour in direction 0 (1, 0) is wall's 1 left side ->
    # new direction will be from wall 2 to 0 (direction 0). New x will be 0, y is unchanged.
    # This is a bit ugly solution - I determined all walls' neighbours by hand on a piece of paper.
    walls_neighbourhood = [
        [
            (1, 0, lambda x, y: (0, y)),
            (2, 1, lambda x, y: (x, 0)),
            (4, 0, lambda x, y: (0, CubicCoords.length-1-y)),
            (5, 0, lambda x, y: (0, x)),
        ],
        [
            (3, 2, lambda x, y: (CubicCoords.length-1, CubicCoords.length-1-y)),
            (2, 2, lambda x, y: (CubicCoords.length-1, x)),
            (0, 2, lambda x, y: (CubicCoords.length-1, y)),
            (5, 3, lambda x, y: (x, CubicCoords.length-1)),
        ],
        [
            (1, 3, lambda x, y: (y, CubicCoords.length-1)),
            (3, 1, lambda x, y: (x, 0)),
            (4, 1, lambda x, y: (y, 0)),
            (0, 3, lambda x, y: (x, CubicCoords.length-1)),
        ],
        [
            (1, 2, lambda x, y: (CubicCoords.length-1, CubicCoords.length-1-y)),
            (5, 2, lambda x, y: (CubicCoords.length-1, x)),
            (4, 2, lambda x, y: (CubicCoords.length-1, y)),
            (2, 3, lambda x, y: (x, CubicCoords.length-1)),
        ],
        [
            (3, 0, lambda x, y: (0, y)),
            (5, 1, lambda x, y: (x, 0)),
            (0, 0, lambda x, y: (0, CubicCoords.length-1-y)),
            (2, 0, lambda x, y: (0, x)),
        ],
        [
            (3, 3, lambda x, y: (y, CubicCoords.length-1)),
            (1, 1, lambda x, y: (x, 0)),
            (0, 1, lambda x, y: (y, 0)),
            (4, 3, lambda x, y: (x, CubicCoords.length-1)),
        ],
    ]

    def __init__(self, wall: int, x: int, y: int, rot: int) -> None:
        self.wall = wall
        self.x = x
        self.y = y
        self.rot = rot

    @classmethod
    def from_board(cls, x: int, y: int, rot: int) -> CubicCoords:
        wall = cls.board_segment_to_wall[(x // cls.length, y // cls.length)]
        return cls(wall, x % cls.length, y % cls.length, rot)
    
    def to_board(self) -> Tuple[int, int, int]:
        bs = self.wall_to_board_segment[self.wall]
        return (bs[0] + self.x, bs[1] + self.y, self.rot)

    def next(self) -> CubicCoords:
        dx, dy = ROTATIONS[self.rot]
        nx = self.x + dx
        ny = self.y + dy
        if 0 <= nx < self.length and 0 <= ny < self.length:
            return CubicCoords(self.wall, nx, ny, self.rot)
        next_wall, new_rot, new_xy_func = self.walls_neighbourhood[self.wall][self.rot]
        nx, ny = new_xy_func(self.x, self.y)
        return CubicCoords(next_wall, nx, ny, new_rot)

    def rotated(self, direction: str) -> CubicCoords:
        if direction == "L":
            return CubicCoords(self.wall, self.x, self.y, (self.rot - 1) % 4)
        if direction == "R":
            return CubicCoords(self.wall, self.x, self.y, (self.rot + 1) % 4)
        raise BaseException(f"unexpected rotation {direction}")
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y}), wall {self.wall}, rot {self.rot}"


class Cube:
    def __init__(self, board: List[str]) -> None:
        self.walls = []
        for x0, y0 in CubicCoords.wall_to_board_segment:
            x1 = x0 + CubicCoords.length
            y1 = y0 + CubicCoords.length
            self.walls.append([row[x0:x1] for row in board[y0:y1]])

    def at(self, cc: CubicCoords) -> str:
        return self.walls[cc.wall][cc.y][cc.x]
        
    def __str__(self) -> str:
        return "\n\n".join("\n".join(w) for w in self.walls)


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
    cube = Cube(board)

    # Sanity check test - go around the cube from each wall in each direction:
    for wall in range(6):
        for rot in range(4):
            wr = set()
            cc = CubicCoords(wall, 10, 30, rot)
            cc0 = cc.__str__()
            wr.add((cc.wall, cc.rot))
            for _ in range(200):
                cc = cc.next()
                wr.add((cc.wall, cc.rot))
            cc1 = cc.__str__()
            if cc0 != cc1:
                print(f"test failed for {cc0} != {cc1}, walls encountered: {sorted(list(wr))}")
    
    # Actual solution:
    cc = CubicCoords.from_board(board[0].index("."), 0, 0)
    for i, steps in enumerate(moves):
        for _ in range(steps):
            ncc = cc.next()
            if cube.at(ncc) == "#":
                break
            cc = ncc
        if i < len(rotations):
            cc = cc.rotated(rotations[i])
    x, y, rot = cc.to_board()
    print(1000*(y+1) + 4*(x+1) + rot)


if __name__ == "__main__":
    main()

