import sys
import enum
from collections import defaultdict

sys.setrecursionlimit(1000000)


class Direction(enum.Enum):
    Left = 0
    Up = 1,
    Right = 2,
    Down = 3,

    def move(self, coord: (int, int)) -> (int, int):
        match self:
            case Direction.Left: return coord[0] - 1, coord[1]
            case Direction.Right: return coord[0] + 1, coord[1]
            case Direction.Down: return coord[0], coord[1] + 1
            case Direction.Up: return coord[0], coord[1] - 1


def trace_beam(curr: (int, int), dir: Direction, path: {(int, int): int}, inp: [[str]]):
    nx, ny = dir.move(curr)
    if nx < 0 or ny < 0 or nx >= len(inp[0]) or ny >= len(inp):
        return

    if dir in path[(nx, ny)]:
        return

    path[(nx, ny)].append(dir)

    match inp[ny][nx]:
        case ".": trace_beam((nx, ny), dir, path, inp)
        case "\\" if dir == Direction.Right: trace_beam((nx, ny), Direction.Down, path, inp)
        case "\\" if dir == Direction.Left: trace_beam((nx, ny), Direction.Up, path, inp)
        case "\\" if dir == Direction.Up: trace_beam((nx, ny), Direction.Left, path, inp)
        case "\\" if dir == Direction.Down: trace_beam((nx, ny), Direction.Right, path, inp)

        case "/" if dir == Direction.Right: trace_beam((nx, ny), Direction.Up, path, inp)
        case "/" if dir == Direction.Left: trace_beam((nx, ny), Direction.Down, path, inp)
        case "/" if dir == Direction.Up: trace_beam((nx, ny), Direction.Right, path, inp)
        case "/" if dir == Direction.Down: trace_beam((nx, ny), Direction.Left, path, inp)

        case "|" if dir in [Direction.Right, Direction.Left]:
            trace_beam((nx, ny), Direction.Up, path, inp)
            trace_beam((nx, ny), Direction.Down, path, inp)
        case "|" if dir in [Direction.Up, Direction.Down]:
            trace_beam((nx, ny), dir, path, inp)

        case "-" if dir in [Direction.Right, Direction.Left]:
            trace_beam((nx, ny), dir, path, inp)
        case "-" if dir in [Direction.Up, Direction.Down]:
            trace_beam((nx, ny), Direction.Left, path, inp)
            trace_beam((nx, ny), Direction.Right, path, inp)

        case _:
            raise NotImplemented


def pathlen(x: int, y: int, dir: Direction, inp: [[int]]) -> int:
    path = defaultdict(list)
    trace_beam((x, y), dir, path, inp)
    return len(path)


def main():
    inp = [list(i) for i in open("data.in").read().split("\n")]

    print(pathlen(-1, 0, Direction.Right, inp))

    longest = 0
    for y in range(0, len(inp)):
        longest = max(longest, pathlen(-1, y, Direction.Right, inp), pathlen(len(inp[0]), y, Direction.Left, inp))
    for x in range(0, len(inp[0])):
        longest = max(longest, pathlen(x, -1, Direction.Down, inp), pathlen(x, len(inp), Direction.Up, inp))
    print(longest)


if __name__ == '__main__':
    main()  
                