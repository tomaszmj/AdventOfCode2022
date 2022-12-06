#!/usr/bin/python

def main():
    stacks = []
    with open("data.txt", "r") as f:
        initial_lines = []
        line = f.readline()
        while "1" not in line:
            initial_lines.append(line)
            line = f.readline()
        positions = []
        for i, c in enumerate(line):
            if c.isdigit():
                positions.append(i)
                stacks.append([])
        for l in reversed(initial_lines):
            for i, p in enumerate(positions):
                if len(l) > p:
                    if l[p].isalpha():
                        stacks[i].append(l[p])
        for line in f:
            line = line.strip()
            if not line:
                continue
            spl = line.split(" ") # move 1 from 2 to 1 -> get 1, 2, 1
            if len(spl) != 6:
                print(f"unexpected line {line}")
                continue
            count = int(spl[1])
            from_stack = int(spl[3])
            to_stack = int(spl[5])
            items = stacks[from_stack-1][-count:]
            stacks[to_stack-1].extend(items)
            stacks[from_stack-1] = stacks[from_stack-1][:-count]
    print("".join(stack[-1] for stack in stacks))


if __name__ == "__main__":
    main()

