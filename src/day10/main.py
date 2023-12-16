import sys
sys.setrecursionlimit(1_000_000)


def neighbors(i: (int, int), curr: str = "S") -> [(int, int)]:
    res = []

    if curr in "-LFS":
        res.append(((i[0] + 1, i[1]), "-J7"))
    if curr in "-J7S":
        res.append(((i[0] - 1, i[1]), "-FL"))
    if curr in "|7FS":
        res.append(((i[0], i[1] + 1), "|LJ"))
    if curr in "|LJS":
        res.append(((i[0], i[1] - 1), "|F7"))

    return res


def all_neighbors(i: (int, int)) -> [(int, int)]:
    return [
        (i[0] + 1, i[1]),
        (i[0] - 1, i[1]),
        (i[0], i[1] + 1),
        (i[0], i[1] - 1),

        (i[0] + 1, i[1] + 1),
        (i[0] - 1, i[1] - 1),
        (i[0] - 1, i[1] + 1),
        (i[0] + 1, i[1] - 1)
    ]


def step(src: (int, int), data: {(int, int): str}, filtered: {(int, int)}, expected=1):
    possibility = []
    for i, allowed in neighbors(src, data[src]):
        try:
            p = data[i]
        except KeyError:
            continue
        if p in allowed and i not in filtered:
            possibility.append(i)

    assert len(possibility) == expected, f"{src} neighbors {possibility}"
    if expected == 1:
        return possibility[0]
    else:
        return possibility


def fill(
        src: (int, int),
        data: {(int, int): str},
        filled: {int, int},
        pipes: {(int, int)},
):
    if src in data and src not in pipes:
        filled.add(src)
    for i in all_neighbors(src):
        if i not in filled and i in data:
            x, y = i
            if i not in pipes:
                fill(i, data, filled, pipes)
                continue


def main():
    inp = [list(i) for i in open("test5.in").read().split("\n")]
    height = len(inp)
    width = len(inp[0])

    data = {}
    start = None
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            data[(x, y)] = c
            if c == "S":
                start = (x, y)
    assert start is not None

    pipes = set()

    n1, n2 = step(start, data, pipes, 2)
    steps = 2
    pipes.add(n1)
    pipes.add(n2)
    while True:
        n1 = step(n1, data, pipes)
        if n1 == n2:
            pipes.add(n1)
            break

        n2 = step(n2, data, pipes)
        if n1 == n2:
            pipes.add(n1)
            pipes.add(n2)
            break

        pipes.add(n1)
        pipes.add(n2)
        steps += 1

    print(steps)


    possible_starts = []
    for x in range(-1, width + 1):
        possible_starts.append((x, -1))
        possible_starts.append((x, height))
    for y in range(-1, height + 1):
        possible_starts.append((-1, y))
        possible_starts.append((width, y))

    outside = set()
    for p in possible_starts:
        fill(p, data, outside, pipes)

    inside = set()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if (x, y) in outside:
                print("_", end="")
            elif (x, y) in pipes:
                print(c, end="")
            else:
                print("I", end="")
                inside.add((x, y))
        print()

    print("outside", len(outside))
    print("inside", len(inside))
    print(len(pipes))


if __name__ == '__main__':
    main()
