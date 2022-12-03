#!/usr/bin/python

def priority(n: str) -> int:
    v = ord(n)
    if v >= ord("a") and v <= ord("z"):
        return v - ord("a") + 1
    if v >= ord("A") and v <= ord("Z"):
        return v - ord("A") + 27
    return 0


def find_item_in_both_compartments(line: str) -> str:
    halflen = len(line) // 2
    left = set()
    for c in line[:halflen]:
        left.add(c)
    found = ""
    for c in line[halflen:]:
        if c in left:
            if found and found != c:
                raise BaseException("multiple items would be found")
            found = c 
    if not found:
        raise BaseException("not found anything")
    return found


def main():
    result = 0
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                item = find_item_in_both_compartments(line)
                result += priority(item)
            except BaseException as e:
                print(f"failed to parse line {line}: {e}")
    print(result)


if __name__ == "__main__":
    main()

