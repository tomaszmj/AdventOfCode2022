#!/usr/bin/python

def main():
    cubes = set()
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if not line:
                    continue
                cubes.add(tuple(int(l) for l in line.split(",")))
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    result = 0
    for c in cubes:
        for coord in range(3):
            for delta in [-1, 1]:
                c2 = tuple(c[i] if i != coord else c[i] + delta for i in range(3))
                if c2 not in cubes:
                    result += 1
    print(result)


if __name__ == "__main__":
    main()

