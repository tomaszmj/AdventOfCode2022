#!/usr/bin/python

ROCK = 0
PAPER = 1
SCISSORS = 2

SHAPE_SCORES = [1, 2, 3]

SHAPES = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

LOSERS = {
    ROCK: SCISSORS,
    SCISSORS: PAPER,
    PAPER: ROCK,
}

WINNERS = {
    SCISSORS: ROCK,
    PAPER: SCISSORS,
    ROCK: PAPER,
}

def score_round(oponent, me: int) -> int:
    shape_score = SHAPE_SCORES[me]
    if oponent == me:
        return shape_score + 3
    if LOSERS[me] == oponent:
        return shape_score + 6
    if LOSERS[oponent] == me:
        return shape_score
    raise BaseException(f"unexpected values: me {me}, oponent {oponent}")


def main():
    score = 0
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            opponent = SHAPES[line[0]]
            r = line[2]
            if r == "X":
                me = LOSERS[opponent]
            elif r == "Y":
                me = opponent
            elif r == "Z":
                me = WINNERS[opponent]
            score += score_round(opponent, me)
    print(score)


if __name__ == "__main__":
    main()

