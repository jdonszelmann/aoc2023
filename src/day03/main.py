from collections import defaultdict


def main():
    inp = open("data.in").read().split("\n")

    symbols = {}
    numbers = defaultdict(list)
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if not c.isdigit() and c != ".":
                res = []
                symbols[(x, y)] = (c, res)
                symbols[(x-1, y)] = (c, res)
                symbols[(x-1, y-1)] = (c, res)
                symbols[(x, y-1)] = (c, res)
                symbols[(x+1, y-1)] = (c, res)
                symbols[(x+1, y)] = (c, res)
                symbols[(x+1, y+1)] = (c, res)
                symbols[(x, y+1)] = (c, res)
                symbols[(x-1, y+1)] = (c, res)
            if c.isdigit():
                if (x - 1, y) in numbers:
                    numbers[(x, y)] = numbers[(x - 1, y)]
                numbers[(x, y)].append(c)

    had = set()
    for loc, num in numbers.items():
        if id(num) in had:
            continue
        if loc in symbols:
            symbols[loc][1].append(int("".join(num)))
            had.add(id(num))

    total = 0
    had = set()
    ok = {}
    for k, s in symbols.items():
        if id(s[1]) in had:
            continue
        had.add(id(s[1]))
        total += sum(s[1])
        ok[k] = s

    print(total)

    ratio_total = 0
    for v in ok.values():
        if v[0] == "*" and len(v[1]) == 2:
            ratio = v[1][0] * v[1][1]
            ratio_total += ratio
    print(ratio_total)


if __name__ == '__main__':
    main()  
                