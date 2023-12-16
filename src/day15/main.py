

def hash(inp: str) -> int:
    curr = 0

    for i in inp:
        curr += ord(i)
        curr *= 17
        curr %= 256

    return curr



def main():
    inp = open("data.in").read().split(",")

    res = 0
    for part in inp:
        res += hash(part)
    print(res)

    hashmap = [[] for i in range(256)]
    for part in inp:
        if part[-1] == "-":
            key = part[:-1]
            h = hash(key)
            hashmap[h] = [(k, v) for k,v in hashmap[h] if k != key]
        else:
            key, value = part.split("=")
            h = hash(key)
            box = hashmap[h]
            for idx, (k, _) in enumerate(box):
                if k == key:
                    box[idx] = (key, value)
                    break
            else:
                box.append((key, value))

    res = 0
    for idx in range(256):
        for lens in range(len(hashmap[idx])):
            res += (idx + 1) * (lens + 1) * int(hashmap[idx][lens][1])

    print(res)


if __name__ == '__main__':
    main()  
                