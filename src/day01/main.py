
def find_num(line: str):
    end = 1

    while True:
        part = line[:end]
        for p in part:
            if p.isdigit():
                return p
        if part.endswith("one") or part.endswith("eno"):
            return "1"
        if part.endswith("two") or part.endswith("owt"):
            return "2"
        if part.endswith("three") or part.endswith("eerht"):
            return "3"
        if part.endswith("four") or part.endswith("ruof"):
            return "4"
        if part.endswith("five") or part.endswith("evif"):
            return "5"
        if part.endswith("six") or part.endswith("xis"):
            return "6"
        if part.endswith("seven") or part.endswith("neves"):
            return "7"
        if part.endswith("eight") or part.endswith("thgie"):
            return "8"
        if part.endswith("nine") or part.endswith("enin"):
            return "9"
        end += 1


def main():
    inp = open("data.in").readlines()

    total = 0
    for line in inp:
        if line.strip() != "":
            fst = find_num(line)
            last = find_num(line[::-1])
            print(fst + last)
            num = int(fst + last)
            total += num

    print(total)


                
if __name__ == '__main__':
    main()  
                