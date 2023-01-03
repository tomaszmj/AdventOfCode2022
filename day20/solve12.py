#!/usr/bin/python
from typing import List


class Numbers:
    def __init__(self, data: List[int], multiplier: int) -> None:
        self.data = [n * multiplier for n in data]
        # doubly-linked circular list implemented in an array
        self.prev = [(i-1) % len(data) for i in range(len(data))]
        self.next = [(i+1) % len(data) for i in range(len(data))]

    def _successor(self, start, steps: int, modulo: int) -> int:
        steps_abs = steps % modulo
        i = start
        for _ in range(steps_abs):
            i = self.next[i]
        return i
    
    # because of finding "successor" iteratively, mix has complexity
    # O(len(data)^2), but this is enough for the data provided
    def mix(self, iterations: int):
        for _ in range(iterations):
            for i, n in enumerate(self.data):
                # "remove" number at position i:
                prev = self.prev[i]
                next = self.next[i]
                self.next[prev] = next
                self.prev[next] = prev
                # "insert" number afer position new_prev
                # ("modulo" is len(self.data) - 1 instead of len(self.data),
                # because we have just "removed" number from the list)
                new_prev = self._successor(prev, n, len(self.data) - 1)
                new_next = self.next[new_prev]
                self.next[new_prev] = i
                self.prev[i] = new_prev
                self.next[i] = new_next
                self.prev[new_next] = i
        result = 0
        i = self.data.index(0)
        for _ in range(3):
            i = self._successor(i, 1000, len(self.data))
            result += self.data[i]
        return result


def main():
    data: List[int] = []
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if line:
                    data.append(int(line))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    print("part1", Numbers(data, 1).mix(1))
    print("part2", Numbers(data, 811589153).mix(10))


if __name__ == "__main__":
    main()

