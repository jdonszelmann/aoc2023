from collections import defaultdict


def main():
    inp = open("data.in").read().split("\n")
    sum_possible = 0
    sum_powers = 0

    for game in inp:
        game_num, rest = game.split(":")
        sets = rest.split(";")
        possible = True
        subgames = defaultdict(list)
        for gameset in sets:
            elems = gameset.split(",")
            outcome = {}
            for color in elems:
                num, name = color.strip().split(" ")
                outcome[name] = int(num)
                subgames[name].append(int(num))


            if outcome.get("red", 0) > 12:
                possible = False

            if outcome.get("green", 0) > 13:
                possible = False

            if outcome.get("blue", 0) > 14:
                possible = False


        mins = {k:max(v) for k, v in subgames.items()}
        power = mins["red"] * mins["green"] * mins["blue"]
        print(f"{game_num}: {possible} with min {mins} giving power {power}")
        if possible:
            sum_possible += int(game_num.split(" ")[1])
        sum_powers += power

    print(sum_possible)
    print(sum_powers)


                
if __name__ == '__main__':
    main()  
                