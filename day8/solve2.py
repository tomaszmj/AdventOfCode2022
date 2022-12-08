#!/usr/bin/python


def count_score(grid: list, x: int, y: int) -> int:
    s1 = count_score_in_direction(grid, x, y, -1, 0)
    s2 = count_score_in_direction(grid, x, y, 1, 0)
    s3 = count_score_in_direction(grid, x, y, 0, -1)
    s4 = count_score_in_direction(grid, x, y, 0, 1)
    return s1*s2*s3*s4


def count_score_in_direction(grid: list, x: int, y: int, dx: int, dy: int) -> int:
    height = grid[y][x]
    x = x + dx
    y = y + dy
    score = 0
    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        score += 1
        if grid[y][x] >= height:
            break
        x = x + dx
        y = y + dy
    return score


def main():
    grid = []
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                grid.append(list(int(c) for c in line))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
    max_score = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            score = count_score(grid, x, y)
            max_score = max(score, max_score)
    print(max_score)


if __name__ == "__main__":
    main()

