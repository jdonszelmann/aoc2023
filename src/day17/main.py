import enum
import heapq


class Node:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value[0] > other.value[0]


class Direction(enum.Enum):
    Left = 0
    Up = 1,
    Right = 2,
    Down = 3,
    No = 4,

    def value(self):
        match self:
            case Direction.Left: return "<"
            case Direction.Right: return ">"
            case Direction.Up: return "^"
            case Direction.Down: return "v"
            case Direction.No: return "x"


def main():
    inp = [[int(i) for i in j] for j in open("test.in").read().split("\n")]

    todo = []
    had = set()
    curr = Node((0, (0, 0), None, Direction.No))
    heapq.heappush(todo, curr)
    best = None

    while len(todo) != 0:
        curr = heapq.heappop(todo)
        cost, pos, parent, direction = curr.value
        cv = (
            cost, pos,
        )
        if cv in had:
            continue

        had.add(cv)

        if pos == (len(inp)-1, len(inp[0])-1):
            best = curr
            break

        for neighbor in [
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
        ]:
            if 0 <= neighbor[0] < len(inp[0]) and 0 <= neighbor[1] < len(inp):
                dx = neighbor[0] - pos[0]
                dy = neighbor[1] - pos[1]

                dir = Direction.No
                match (dx, dy):
                    case (-1, 0): dir = Direction.Left
                    case (1, 0): dir = Direction.Right
                    case (0, -1): dir = Direction.Up
                    case (0, 1): dir = Direction.Down

                if parent is not None:
                    match (curr.value[3], dir):
                        case (Direction.Left, Direction.Right): continue
                        case (Direction.Up, Direction.Down): continue
                        case (Direction.Right, Direction.Left): continue
                        case (Direction.Down, Direction.Up): continue

                last_dirs = []
                x = curr
                for i in range(10):
                    d = x.value[3]
                    if d != Direction.No:
                        last_dirs.append(d)
                    x = curr.value[2]
                    if x is None:
                        break

                if len(last_dirs) == 10 and all(dir == last_dirs[0] for i in last_dirs):
                    continue
                if any(dir != last_dirs[0] for i in last_dirs[:4]):
                    continue

                if (neighbor[0], neighbor[1]) in had:
                    continue

                heapq.heappush(todo, Node((cost + inp[neighbor[1]][neighbor[0]], neighbor, curr, dir)))

    curr = best
    heat_loss = curr.value[2].value[0]
    path = {}
    while curr is not None:
        path[curr.value[1]] = curr.value[3]
        curr = curr.value[2]

    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if (x, y) in path:
                print("\u001b[37;1m" + path[(x, y)].value() + "\u001b[0m", end="")
            else:
                print(inp[y][x], end="")
        print()

    print(heat_loss)

if __name__ == '__main__':
    main()
