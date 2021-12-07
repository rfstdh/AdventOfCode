DAY_RANGE = 256

with open("input6.txt") as file:
    data = [int(line) for line in file.read().split(",")]
    bornlist = [data.count(x) for x in range(9)]
    fishes = len(data)
    tmplist = bornlist
    for day in range(DAY_RANGE):
        bornlist = tmplist
        val = bornlist[0]
        del bornlist[0]
        if(val > 0):
            bornlist.append(val)
            bornlist[6] += val
        else:
            bornlist.append(val)
    #part 1 and part 2
    print(sum(bornlist))