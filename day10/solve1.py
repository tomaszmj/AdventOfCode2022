#!/usr/bin/python

def main():
    cycles_to_check = {20, 60, 100, 140, 180, 220}
    cycle = 0
    x = 1
    result = 0
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if line.startswith("noop"):
                    cycle += 1
                    if cycle in cycles_to_check:
                        result += x*cycle
                        #print(f"add1 at cycle {cycle} (after noop), X {x}")
                elif line.startswith("addx"):
                    number = int(line.split(" ")[1])
                    cycle += 1
                    if cycle in cycles_to_check:
                        result += x*cycle
                        #print(f"add2 at cycle {cycle} (during first cycle of addx {number}), X {x}")
                    cycle += 1
                    if cycle in cycles_to_check:
                        result += x*cycle
                        #print(f"add3 at cycle {cycle} (during second cycle of addx {number}), X {x}")
                    x += number
                else:
                    raise BaseException("unknown command")
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    print(result)


if __name__ == "__main__":
    main()

