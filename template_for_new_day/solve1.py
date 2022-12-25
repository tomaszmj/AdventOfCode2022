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


def main():
    with open("data_small.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                print(line)
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    print(f"done")


if __name__ == "__main__":
    main()

