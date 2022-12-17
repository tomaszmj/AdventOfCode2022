#!/usr/bin/python
import json
import functools


def compare(left, right) -> int:
    if type(left) == list:
        if type(right) == list:
            return compare_lists(left, right)
        return compare_lists(left, [right])
    if type(right) == list:
        return compare_lists([left], right)
    return compare_ints(left, right)


def compare_ints(left: int, right: int) -> int:
    if type(left) != int or type(right) != int:
        raise BaseException(f"cannot compare_ints, got types {type(left)}, {type(right)}")
    return left - right


def compare_lists(left: list, right: list) -> int:
    if type(left) != list or type(right) != list:
        raise BaseException(f"cannot compare_lists, got types {type(left)}, {type(right)}")
    for l, r in zip(left, right):
        cmp = compare(l, r)
        if cmp:
            return cmp
    return len(left) - len(right)


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
    data.append([[6]])
    data.append([[2]])
    data.sort(key=functools.cmp_to_key(compare))
    result = 1
    for i, d in enumerate(data):
        if d == [[6]] or d == [[2]]:
            result *= i+1
    print(result)


if __name__ == "__main__":
    main()

