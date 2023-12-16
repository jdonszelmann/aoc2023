import functools
from math import gcd

def steps_for_a(start: str, instructions: str, network: {str: {str: str}}) -> int:
    curr = start
    steps = 0
    while True:
        for instruction in instructions:
            curr = network[curr][instruction]
            steps += 1

            if curr[-1] == "Z":
                return steps


def main():
    instructions, lines = open("data.in").read().split("\n\n")

    network = {}
    for line in lines.split("\n"):
        src, left,  right = line.replace("(", "").replace(")", "").replace("=", ",").replace(",", "").split()
        network[src] = {"L": left, "R": right}

    print(steps_for_a("AAA", instructions, network))

    lcm = functools.reduce(lambda a,i: a * (i//gcd(a, i)), [steps_for_a(i, instructions, network) for i in network if i[-1] == "A"], 1)
    print(lcm)





if __name__ == '__main__':
    main()  
                