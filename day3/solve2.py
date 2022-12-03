#!/usr/bin/python

def priority(n: str) -> int:
    v = ord(n)
    if v >= ord("a") and v <= ord("z"):
        return v - ord("a") + 1
    if v >= ord("A") and v <= ord("Z"):
        return v - ord("A") + 27
    return 0


def find_item_in_3_rucksacks(lines) -> str:
    common_items = set()
    for line in lines:
        s = set(line)
        if not common_items:
            common_items = s
        else:
            common_items.intersection_update(s)
    if len(common_items) != 1:
        raise BaseException(f"expected 1 common item, got {common_items}")
    return common_items.pop()


def main():
    result = 0
    lines = []
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lines.append(line)
    for i in range(0, len(lines), 3):
        try:
            item = find_item_in_3_rucksacks(lines[i:i+3])
            result += priority(item)
        except BaseException as e:
            print(f"failed to process lines at index {i}: {e}")
    print(result)


if __name__ == "__main__":
    main()
