import numpy as np


class Digger:
    def __init__(self):
        self.pos = [0, 0]
        self.seen = [list(tuple(self.pos))]
        self.distance_moved = 0

    def moved(self):
        self.seen.append(list(tuple(self.pos)))

    def right(self, num: int):
        self.distance_moved += num
        self.pos[0] += num
        self.moved()

    def left(self, num: int):
        self.distance_moved += num
        self.pos[0] -= num
        self.moved()

    def up(self, num: int):
        self.distance_moved += num
        self.pos[1] -= num
        self.moved()

    def down(self, num: int):
        self.distance_moved += num
        self.pos[1] += num
        self.moved()

    def area(self) -> {(int, int)}:
        lines = np.hstack([self.seen,np.roll(self.seen,-1,axis=0)])
        area = abs(sum(x1*y2-x2*y1 for x1,y1,x2,y2 in lines)) // 2
        return area + self.distance_moved // 2 + 1


def main():
    inp = open("data.in").read().split("\n")

    d = Digger()
    t = Digger()
    for line in inp:
        rot, num, color = line.split(" ")
        match rot:
            case "R": d.right(int(num))
            case "L": d.left(int(num))
            case "U": d.up(int(num))
            case "D": d.down(int(num))

        num = int(color[2:7], 16)
        match int(color[7]):
            case 0: t.right(num)
            case 2: t.left(num)
            case 3: t.up(num)
            case 1: t.down(num)

    print(d.area())
    print(t.area())


if __name__ == '__main__':
    main()  
                