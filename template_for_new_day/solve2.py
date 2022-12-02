#!/usr/bin/python

def main():
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
    print(f"done")


if __name__ == "__main__":
    main()

