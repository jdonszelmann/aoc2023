import functools



def main():
    inp = open("data.in").read().split("\n")

    # total_points = 0
    games = {}
    for line in inp:
        card, line = line.split(":")
        card = int(card.split()[1])
        left, right = line.split("|")
        left = [int(i) for i in left.split()]
        right = [int(i) for i in right.split()]
        games[card] = (left, right)

        # winning = [i for i in left if i in right]
        # points = 0
        # if len(winning) != 0:
        #     points = 1
        #     for _ in winning[1:]:
        #         points *= 2
        # print(points)
        # total_points += points
    # print(total_points)

    @functools.cache
    def game(draw: int):
        numbers, our_draw = games[draw]

        num_winning = len([i for i in numbers if i in our_draw])
        total_cards = 0
        for i in range(draw + 1, draw + 1 + num_winning):
            total_cards += game(i)

        return total_cards + 1


    total_cards = sum(game(i) for i in range(1, len(games) + 1))
    print(total_cards)


if __name__ == '__main__':
    main()  
                