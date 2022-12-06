#!/usr/bin/python

def main():
    with open("data.txt", "r") as f:
        l = f.readline()
    for i in range(14, len(l)):
        chars = l[i-14:i]
        unique_chars = set(chars)
        if len(unique_chars) != 14:
            continue
        print(i)
        break

if __name__ == "__main__":
    main()

