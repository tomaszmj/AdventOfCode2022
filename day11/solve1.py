#!/usr/bin/python
from typing import List, Tuple


class MonkeyOperation:
    def __init__(self, op: str) -> None:
        op_split = op.split(" * ")
        if len(op_split) == 2:
            self.operator = "*"
        else:
            op_split = op.split(" + ")
            if len(op_split) != 2:
                raise BaseException("unexpected operation format")
            self.operator = "+"
        if op_split[0] == "old":
            self.operand1 = None
        else:
            self.operand1 = int(op_split[0])
        if op_split[1] == "old":
            self.operand2 = None
        else:
            self.operand2 = int(op_split[1])

    def __call__(self, old: int) -> int:
        n1 = old if self.operand1 is None else self.operand1
        n2 = old if self.operand2 is None else self.operand2
        if self.operator == "*":
            return n1 * n2
        else:
            return n1 + n2


class Monkey:
    def __init__(
        self, 
        starting_items: List[int],
        operation: MonkeyOperation,
        divisible_by: int,
        if_true_throw: int,
        if_false_throw: int,
    ) -> None:
        self.items = starting_items
        self.operation = operation
        self.divisible_by = divisible_by
        self.if_true_throw = if_true_throw
        self.if_false_throw = if_false_throw
        self.inspect_item_counts = 0

    # inspect_items returns list of (worry level, monkey number)
    def inspect_items(self) -> List[Tuple[int, int]]:
        result = []
        for item in self.items:
            self.inspect_item_counts += 1
            worry_level = self.operation(item) // 3
            if worry_level % self.divisible_by == 0:
                result.append((worry_level, self.if_true_throw))
            else:
                result.append((worry_level, self.if_false_throw))
        self.items = []
        return result

    def add_item(self, item: int) -> None:
        self.items.append(item)


def readline_and_partition(file, partition_key: str) -> str:
    line = file.readline().rstrip()
    _, _, suffix = line.partition(partition_key)
    if not suffix:
        raise BaseException(f"failed to partition line by {partition_key}")
    return suffix


def main():
    monkeys: List[Monkey] = []
    with open("data.txt", "r") as f:
        line = f.readline()
        try:
            while line:
                line = line.rstrip()
                if line != f"Monkey {len(monkeys)}:":
                    raise BaseException("unexpected line")
                si_str = readline_and_partition(f, "  Starting items: ")
                si = list(int(i) for i in si_str.split(", "))
                op_str = readline_and_partition(f, "  Operation: new = ")
                op = MonkeyOperation(op_str) 
                div = readline_and_partition(f, "  Test: divisible by ")
                if_true = readline_and_partition(f, "    If true: throw to monkey ")
                if_false = readline_and_partition(f, "    If false: throw to monkey ")
                monkeys.append(Monkey(si, op, int(div), int(if_true), int(if_false)))
                line = f.readline() # empty line between monkeys
                if not line:
                    break
                line = f.readline()
        except BaseException as e:
            print(f"error parsing line ({line}): {e}")
            raise
    for _ in range(20):
        for monkey in monkeys:
            result = monkey.inspect_items()
            for r in result:
                monkeys[r[1]].add_item(r[0])
    monkeys.sort(key=lambda m: m.inspect_item_counts, reverse=True)
    print(monkeys[0].inspect_item_counts * monkeys[1].inspect_item_counts)


if __name__ == "__main__":
    main()

