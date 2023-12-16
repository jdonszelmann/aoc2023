from collections import defaultdict
from functools import cache

import numpy as np
from tqdm import tqdm


def roll(inp):
    for row in range(len(inp), 0, -1):
        y = len(inp) - row
        for cy in range(y, 0, -1):
            for cx in range(0, len(inp[0])):
                if inp[cy][cx] == "O" and inp[cy - 1][cx] == ".":
                    inp[cy - 1][cx] = inp[cy][cx]
                    inp[cy][cx] = "."


def calc(inp):
    total_load = 0
    for row in range(len(inp), 0, -1):
        y = len(inp) - row
        for x in range(0, len(inp[0])):
            if inp[y][x] == "O":
                total_load += row

    return total_load


def pattern(hist):
    occurences = defaultdict(int)

    for pat_len in range(2, 100):
        pat = hist[-pat_len:]

        for i in range(len(hist)-pat_len, 10, -pat_len):
            subseq = hist[i:i+pat_len]
            if subseq == pat:
                occurences[tuple(pat)] += 1
            else:
                break

    common_seq = max(occurences.items(), key=lambda i: i[1])[0]

    return common_seq


def cycle(inp):
    for _ in range(4):
        roll(inp)
        inp = np.rot90(inp)
        inp = np.rot90(inp)
        inp = np.rot90(inp)


def main():
    inp = np.array([list(i) for i in open("data.in").read().split("\n")])

    hist = []
    first = 200

    for _ in tqdm(range(first)):
        cycle(inp)
        hist.append(calc(inp))

    pat = pattern(hist)
    print(len(pat))
    total = 1000000000
    curr = first
    while (curr + len(pat)) < total:
        curr += len(pat)
    print(curr)

    while curr < total:
        cycle(inp)
        curr += 1

    print(calc(inp))

                
if __name__ == '__main__':
    main()  
                