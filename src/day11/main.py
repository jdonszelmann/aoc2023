from collections import defaultdict
from tqdm import tqdm


def main():
    galaxies = open("data.in").read().split("\n")

    row_expanded_galaxies = []
    for line in tqdm(galaxies):
        if "#" in line:
            row_expanded_galaxies.append(line)
        else:
            for i in range(1_000_000):
                row_expanded_galaxies.append(line)

    transpose_row_expanded_galaxies = list(zip(*row_expanded_galaxies))

    expanded = set()
    column_expanded_galaxies = []
    ctr = 0
    for line in tqdm(transpose_row_expanded_galaxies):
        if "#" in line:
            ctr += 1
            column_expanded_galaxies.append(line)
        else:
            for _ in range(1_000_000):
                expanded.add(ctr)
                ctr += 1
                column_expanded_galaxies.append(line)

    galaxy_locations = set()
    for y in tqdm(range(len(column_expanded_galaxies))):
        if y in expanded:
            continue

        for x in range(len(column_expanded_galaxies[y])):
            if column_expanded_galaxies[y][x] == "#":
                galaxy_locations.add((x, y))

    total_dist = 0
    for loc1 in galaxy_locations:
        for loc2 in galaxy_locations:
            dx = abs(loc1[0] - loc2[0])
            dy = abs(loc1[1] - loc2[1])
            dist = dx + dy
            total_dist += dist

    print(total_dist // 2)


if __name__ == '__main__':
    main()  
                