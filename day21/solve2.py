#!/usr/bin/python
from __future__ import annotations
from typing import Dict, Tuple


class Monkey:
    def __init__(self, line: str, monkey_dict: Dict[str, Monkey]) -> None:
        self.monkey_dict = monkey_dict
        self.name = line[:4]
        self.number = None
        self.left = ""
        self.right = ""
        self.operator = ""
        if len(line) == len("root: pppw + sjmn"):
            self.operator = line[11]
            if self.operator not in "+-/*":
                raise BaseException(f"unexpected operator {self.operator}")
            self.left = line[6:10]
            self.right = line[13:]
        else:
            self.number = int(line[6:])
    
    # yell result is symbolically encoded as tuple (a, b)
    # (real result is ax + b, x being result of "humn" yell)
    def yell(self) -> Tuple[int, int]:
        if self.name == "humn":
            return (1, 0)
        if self.number is not None:
            return (0, self.number)
        left = self.monkey_dict[self.left].yell()
        right = self.monkey_dict[self.right].yell()
        if self.operator == "+":
            return (left[0] + right[0], left[1] + right[1])
        if self.operator == "-":
            return (left[0] - right[0], left[1] - right[1])
        if self.operator == "*":
            if left[0] == 0:
                return (left[1] * right[0], left[1] * right[1])
            if right[0] == 0:
                return (left[0] * right[1], left[1] * right[1])
            # this would make the eqaution polynomial:
            raise BaseException(f"cannot compute yell({self.name}) symbolically: {left} * {right}")
        if self.operator == "/":
            if right[0] != 0 or right[1] == 0:
                # this would introduce division by function of "x" or by 0:
                raise BaseException(f"cannot compute yell({self.name}) symbolically: {left} / {right}")
            return (left[0] / right[1], left[1] / right[1])


def main():
    monkeys: Dict[str, Monkey] = {}
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if not line:
                    continue
                monkey = Monkey(line, monkeys)
                monkeys[monkey.name] = monkey
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    root = monkeys["root"]
    left = monkeys[root.left]
    right = monkeys[root.right]
    l = left.yell()
    r = right.yell()
    # Solve the equation: l[0]*x + l[1] = r[0] * x + r[1]
    x = (r[1] - l[1]) / (l[0] - r[0])
    # Due to lack of numerical precision result is a float.
    # I brutally rounded it when submitting the answer.
    print(x)


if __name__ == "__main__":
    main()

