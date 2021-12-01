#load the data
with open("./Inputs/input1.txt") as file:
    data = [int(line) for line in file.read().splitlines()]
    result = sum([el1 < el2 for el1,el2 in zip(data, data[1:])])
    #part1 - number of elements larger than the previous one
    print(result)
    #part2 - number of three elements which sum is  larger than the sum of previous three elements
    result2 = sum([sum(pair[:3]) < sum(pair[1:]) for pair in zip(data,data[1:],data[2:],data[3:])])
    print(result2)