#!/usr/bin/python
from __future__ import annotations
from typing import Dict


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
    
    def yell(self) -> int:
        if self.number is not None:
            return self.number
        left = self.monkey_dict[self.left].yell()
        right = self.monkey_dict[self.right].yell()
        if self.operator == "+":
            return left + right
        if self.operator == "-":
            return left - right
        if self.operator == "*":
            return left * right
        if self.operator == "/":
            return left / right


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
    print(int(monkeys["root"].yell()))


if __name__ == "__main__":
    main()

