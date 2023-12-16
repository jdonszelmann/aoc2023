import collections
import functools
import itertools

card_ranking_p1 = "23456789TJQKA"
card_ranking_p2 = "J23456789TQKA"


@functools.cache
def rank(hand: (str, ...)) -> int:
    occurrences = [hand.count(i) for i in hand]
    if 5 in occurrences:
        return 7
    elif 4 in occurrences:
        return 6
    elif 3 in occurrences and 2 in occurrences:
        return 5
    elif 3 in occurrences and occurrences.count(1) == 2:
        return 4
    elif occurrences.count(2) == 4 and 1 in occurrences:
        return 3
    elif 2 in occurrences and occurrences.count(1) == 3:
        return 2
    elif occurrences.count(1) == 5:
        return 1
    else:
        print(occurrences)
        return 0


def compare(hand1, hand2) -> int:
    if rank(hand1) > rank(hand2):
        return 1
    elif rank(hand2) > rank(hand1):
        return -1
    else:
        for i in range(0, 5):
            ranking1 = card_ranking_p1.index(hand1[i])
            ranking2 = card_ranking_p1.index(hand2[i])
            if ranking1 > ranking2:
                return 1
            elif ranking2 > ranking1:
                return -1

        return 0


def replace(hand, jokers, replacement):
    hand = list(hand)
    for pos, new in zip(jokers, replacement):
        hand[pos] = new

    return tuple(hand)


@functools.cache
def find_best_rank(hand) -> int:
    jokers = [index for index, i in enumerate(hand) if i == "J"]
    replacements = list(itertools.product(*[card_ranking_p1 for i in range(len(jokers))]))

    best_rank = max(rank(replace(hand, jokers, replacement)) for replacement in replacements)
    return best_rank


def compare_p2(hand1, hand2):
    rank1 = find_best_rank(hand1)
    rank2 = find_best_rank(hand2)

    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return -1
    else:
        for i in range(0, 5):
            ranking1 = card_ranking_p1.index(hand1[i])
            ranking2 = card_ranking_p1.index(hand2[i])
            if ranking1 > ranking2:
                return 1
            elif ranking2 > ranking1:
                return -1

        return 0


def main():
    inp = open("data.in").read().split("\n")

    hands = []
    bids = {}
    for line in inp:
        hand, bid = line.split(" ")
        hands.append(tuple(hand))
        bids[tuple(hand)] = bid

    hands.sort(key=functools.cmp_to_key(compare))
    res = 0
    for index, i in enumerate(hands):
        res += (index+1) * int(bids[i])
    print(res)

    hands.sort(key=functools.cmp_to_key(compare_p2))
    res = 0
    for index, i in enumerate(hands):
        res += (index+1) * int(bids[i])
    print(res)


if __name__ == '__main__':
    main()

