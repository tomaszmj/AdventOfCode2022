#!/usr/bin/python


class Screen:
    def __init__(self) -> None:
        self.screen = list(list("."*40) for _ in range(6))
        self.cycle = 0
        self.x = 1

    def noop(self) -> None:
        self.next_cycle()

    def addx(self, number: int) -> None:
        self.next_cycle()
        self.next_cycle()
        self.x += number

    def next_cycle(self) -> None:
        self.cycle += 1
        x = (self.cycle - 1) % 40  # cycles are counted from 1, while pixels from 0
        y = (self.cycle - 1) // 40
        if abs(x - self.x) <= 1:
            self.screen[y][x] = "#"

    def __str__(self) -> str:
        return "\n".join("".join(s for s in row) for row in self.screen)
    

def main():
    s = Screen()
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if line.startswith("noop"):
                    s.noop()
                elif line.startswith("addx"):
                    number = int(line.split(" ")[1])
                    s.addx(number)
                else:
                    raise BaseException("unknown command")
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    print(s)


if __name__ == "__main__":
    main()

