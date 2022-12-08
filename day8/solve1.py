#!/usr/bin/python


def is_visible(grid: list, x: int, y: int) -> bool:
     return any([
        is_visible_in_direction(grid, x, y, -1, 0),
        is_visible_in_direction(grid, x, y, 1, 0),
        is_visible_in_direction(grid, x, y, 0, -1),
        is_visible_in_direction(grid, x, y, 0, 1),
    ])


def is_visible_in_direction(grid: list, x: int, y: int, dx: int, dy: int) -> bool:
    height = grid[y][x]
    x = x + dx
    y = y + dy
    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        if grid[y][x] >= height:
            return False
        x = x + dx
        y = y + dy
    return True


def main():
    grid = []
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                grid.append(list(int(c) for c in line))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_visible(grid, x, y):
                count += 1
    print(count)


if __name__ == "__main__":
    main()

