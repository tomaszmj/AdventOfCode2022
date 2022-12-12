#!/usr/bin/python

def main():
    with open("data_small.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                print(line)
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    print(f"done")


if __name__ == "__main__":
    main()

