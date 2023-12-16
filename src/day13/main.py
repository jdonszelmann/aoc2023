import copy
from typing import Optional


def reflect_row_equal(row: [str], axis: int) -> bool:
    cur = 1
    while (axis - cur >= 0) and (axis + cur - 1 < len(row)):
        if row[axis - cur] != row[axis + cur - 1]:
            return False
        cur += 1
    return True


def reflect_equal(pattern: [str], axis: int) -> bool:
    for row in pattern:
        if not reflect_row_equal(row, axis):
            return False
    return True


def find_vertical_reflections(pattern: [[str]], old: Optional[int]) -> int | None:
    width = len(pattern[0])
    for i in range(1,width):
        if reflect_equal(pattern, i):
            if old is not None and i == old:
                continue
            return i
    return


def find_horizontal_reflections(pattern: [[str]], old: Optional[int]) -> int:
    transpose = ["".join(i) for i in zip(*pattern)]
    return find_vertical_reflections(transpose, old)


def find_reflection(pattern: [[str]], old: Optional[tuple[bool, int]]) -> Optional[tuple[bool, int]]:
    reflection_col = find_vertical_reflections(pattern, old[1] if old is not None and not old[0] else None)
    if reflection_col is not None:
        assert reflection_col != 0
        return False, reflection_col
    else:
        reflection_row = find_horizontal_reflections(pattern, old[1] if old is not None and old[0] else None)
        if reflection_row is None:
            return
        else:
            return True, reflection_row


def find_different_reflection(pattern: [str]):
    initial = find_reflection(pattern, None)
    assert initial is not None

    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            new_pattern = copy.deepcopy(pattern)
            if new_pattern[y][x] == ".":
                new_pattern[y][x] = "#"
            else:
                new_pattern[y][x] = "."
            new_reflection = find_reflection(new_pattern, initial)

            if new_reflection is not None and new_reflection != initial:
                return new_reflection

    assert False


def main():
    inp = open("data.in").read().split("\n\n")

    res = 0
    for i in inp:
        horizontal, num = find_reflection([list(x) for x in i.split("\n")], None)
        if horizontal:
            num *= 100
        res += num

    print(res)
    res = 0
    for i in inp:
        horizontal, num = find_different_reflection([list(x) for x in i.split("\n")])
        if horizontal:
            num *= 100
        res += num

    print(res)


if __name__ == '__main__':
    main()  
                