#!/usr/bin/python
import json


def compare(left, right):  # -> bool or None
    if type(left) == list:
        if type(right) == list:
            return compare_lists(left, right)
        return compare_lists(left, [right])
    if type(right) == list:
        return compare_lists([left], right)
    return compare_ints(left, right)


def compare_ints(left: int, right: int):  # -> bool or None
    if type(left) != int or type(right) != int:
        raise BaseException(f"cannot compare_ints, got types {type(left)}, {type(right)}")
    if left == right:
        return None
    return left < right


def compare_lists(left: list, right: list):  # -> bool or None
    if type(left) != list or type(right) != list:
        raise BaseException(f"cannot compare_lists, got types {type(left)}, {type(right)}")
    for l, r in zip(left, right):
        cmp = compare(l, r)
        if cmp is not None:
            return cmp
    if len(right) == len(left):
        return None
    return len(right) > len(left)


def main():
    data = []
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if not line:
                    continue
                data.append(json.loads(line))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    left = [data[i] for i in range(0, len(data), 2)]
    right = [data[i] for i in range(1, len(data), 2)]
    result = 0
    for i, data in enumerate(zip(left, right)):
        cmp = compare_lists(data[0], data[1])
        if cmp is None:
            # it should not happen
            print(f"cannot compare lists {data[0]}, {data[1]}")
        if cmp == True:
            result += i + 1
    print(result)


if __name__ == "__main__":
    main()

