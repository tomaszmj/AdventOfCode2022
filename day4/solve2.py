#!/usr/bin/python

import itertools

def main():
    result = 0
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            elfs = line.split(",")
            e1 = list(int(x) for x in elfs[0].split("-"))
            e2 = list(int(x) for x in elfs[1].split("-"))
            if e2[0] < e1[0]:
                e1, e2 = e2, e1 
            if e1[1] >= e2[0]:
                result += 1
    print(result)


if __name__ == "__main__":
    main()

