#!/usr/bin/python

def main():
    with open("data_small.txt", "r") as f:
        for line in f:
            line = line.strip()
            print(line)
    print(f"done")


if __name__ == "__main__":
    main()

