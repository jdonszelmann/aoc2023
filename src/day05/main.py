import typing
from collections import defaultdict
from typing import Self


class Range:
    def __init__(self, start, length = None):
        if isinstance(start, typing.Iterable):
            i = iter(start)
            start = next(i)
            length = next(i)

        assert length is not None

        self.start = start
        self.length = length

    @classmethod
    def empty(cls):
        return cls(0, 0)

    @classmethod
    def from_start_end(cls, start, end):
        res = cls(start, max(end-start, 0))
        if res.length == 0:
            return cls.empty()

        return res

    @property
    def end(self):
        return self.start + self.length

    def __len__(self):
        return self.length

    def __eq__(self, other: Self):
        assert isinstance(other, self.__class__)
        return self.start == other.start and self.length == other.length

    def __repr__(self):
        return f"Range({self.start}, {self.length})"

    def overlap(self, other: Self):
        return self.__class__.from_start_end(max(self.start, other.start), min(self.end, other.end))

    def __contains__(self, item):
        assert isinstance(item, int)
        return self.start <= item < self.end

    def __hash__(self):
        return hash((self.start, self.end))

    def leftover(self, other):
        if self.overlap(other) == Range.empty():
            return []

        return [i for i in [
            Range.from_start_end(min(self.start, other.start), max(self.start, other.start)),
            Range.from_start_end(min(self.end, other.end), max(self.end, other.end)),
        ] if i != Range.empty()]


assert Range(0, 10).overlap(Range(5, 10)) == Range(5, 5)
assert Range(5, 5).overlap(Range(5, 5)) == Range(5, 5)
assert Range(5, 10).overlap(Range(0, 10)) == Range(5, 5)
assert Range(5, 10).overlap(Range(20, 10)) == Range.empty()
assert Range(0, 10).leftover(Range(2, 2)) == [Range(0, 2), Range.from_start_end(4, 10)]
assert Range(2, 2).leftover(Range(2, 2)) == []
assert Range(2, 2).leftover(Range(0, 10)) == [Range(0, 2), Range.from_start_end(4, 10)]
assert Range(2, 2).leftover(Range(4, 2)) == []


def main():
    seeds, maps = open("data.in").read().split("\n", maxsplit=1)
    maps = [i.split("\n") for i in maps.split("\n\n")]
    data: {str: {str: {Range: int}}} = defaultdict(lambda: defaultdict(dict))

    for m in maps:
        src, _, target = m[0].split(" ")[0].split("-")
        lines = [[int(i) for i in line.split()] for line in m[1:]]
        for line in lines:
            data[src][target][Range(line[1], line[2])] = line[0]

    def do_map(nums, map_from):
        k, mapping = next(iter(data[map_from].items()))

        new_nums = []
        had = set()
        while len(nums) != 0:
            i = nums.pop()
            overlaps_one = False
            for src, dst in mapping.items():
                sc: Range
                if isinstance(i, int):
                    if i in src:
                        offset = i - src.start
                        new_nums.append(dst + offset)
                        overlaps_one = True
                        break
                else:
                    overlap = i.overlap(src)
                    if overlap != Range.empty():
                        offset = src.start - dst
                        new_nums.append(Range(overlap.start - offset, overlap.length))
                        l = [x for x in i.leftover(src) if x not in had and x.overlap(i) != Range.empty()]
                        for x in l:
                            had.add(x)
                        nums.extend(l)
                        overlaps_one = True

            if isinstance(i, int) and not overlaps_one:
                new_nums.append(i)
            elif not overlaps_one:
                new_nums.append(i)

        if k == "location":
            return min([i if isinstance(i, int) else i.start for i in new_nums])
        else:
            return do_map(new_nums, k)

    inp = [int(i) for i in seeds.split()[1:]]
    ranges = [Range(inp[i:i + 2]) for i in range(0, len(inp), 2)]
    print(do_map(inp, "seed"))
    print(do_map(ranges, "seed"))


if __name__ == '__main__':
    main()  
                