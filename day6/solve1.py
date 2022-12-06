#!/usr/bin/python

def main():
    with open("data.txt", "r") as f:
        l = f.readline()
    for i in range(4, len(l)):
        chars = l[i-4:i]
        unique_chars = set(chars)
        if len(unique_chars) != 4:
            continue
        print(i)
        break

if __name__ == "__main__":
    main()

