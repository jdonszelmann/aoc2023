def ways_to_beat_record(time: int, record: int) -> int:
    ways_to_beat = 0
    for holding_time in range(1, time):
        speed = holding_time
        time_left = time - holding_time
        distance_travelled = speed * time_left

        if distance_travelled > record:
            ways_to_beat += 1
    return ways_to_beat


def main():
    inp = open("data.in").read().split("\n")

    times, records = [[int(i.strip()) for i in inp[m].split(":")[1].split() if i.strip()!=""]for m in [0, 1]]

    total = 1
    for (time, record) in zip(times, records):
        total *= ways_to_beat_record(time, record)
    print(total)

    time = int(inp[0].split(":")[1].replace(" ", ""))
    record = int(inp[1].split(":")[1].replace(" ", ""))
    print(ways_to_beat_record(time, record))


if __name__ == '__main__':
    main()  
                