#!/usr/bin/python

def snafu_to_decimal(snafu: str) -> int:
    decimal = 0
    power = 1
    for c in reversed(snafu):
        if c == "-":
            n = -1
        elif c == "=":
            n = -2
        else:
            n = int(c)
        decimal += n * power
        power *= 5
    return decimal


def decimal_to_snafu(decimal: int) -> str:
    result = []
    while decimal:
        quotient = decimal // 5
        remainder = decimal % 5
        if remainder > 2:
            remainder -= 5
            quotient += 1
        if remainder == -2:
            result.append("=")
        elif remainder == -1:
            result.append("-")
        else:
            result.append(str(remainder))
        decimal = quotient
    return "".join(reversed(result))


def main():
    sum_decimal = 0
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.strip()
                if line:
                    sum_decimal += snafu_to_decimal(line)
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    print(decimal_to_snafu(sum_decimal))


if __name__ == "__main__":
    main()

