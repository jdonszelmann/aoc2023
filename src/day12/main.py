from functools import cache

from tqdm import tqdm


@cache
def search(inp: (str, ...), nums: (int, ...), started_sequence: bool = False, just_ended: bool = False) -> int:
    if len(nums) == 0:
        return "#" not in inp
    if len(inp) == 0:
        return nums == (0,)

    first_inp, *rest_inp = inp
    first, *rest = nums

    if first == 0:
        return search(inp, tuple(rest), False, True)
    elif first_inp == ".":
        return 0 if started_sequence else search(tuple(rest_inp), nums, False, False)
    elif first_inp == "#":
        return 0 if just_ended else search(tuple(rest_inp), (first - 1, *rest), True, False)
    elif first_inp == "?":
        # it's a dot
        p1 = 0 if started_sequence else search((".", *rest_inp), nums, False, just_ended)
        # it's a hashtag
        p2 = search(("#", *rest_inp), nums, started_sequence, just_ended)
        return p1 + p2


def num_arrangements(row: str, part2: bool = False) -> int:
    records, nums = row.split(" ")

    if part2:
        records = "?".join(records for _ in range(5))
        nums = ",".join(nums for _ in range(5))

    res = search(tuple(records), tuple([int(i) for i in nums.split(",")]))
    return res


def main():
    inp = open("data.in").read().split("\n")

    total = 0
    for row in tqdm(inp):
        total += num_arrangements(row)

    print(total)

    total2 = 0
    for row in tqdm(inp):
        total2 += num_arrangements(row, True)
    print(total2)


if __name__ == '__main__':
    main()
