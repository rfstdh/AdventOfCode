with open("input2.txt") as file:
    data = [line.split(" ") for line in file.read().splitlines()]
    #part1
    depth, horizontal = 0, 0
    for line in data:
        direction = line[0]
        value = int(line[1])
        if (direction == "forward"):
            horizontal += value
        elif (direction == "down"):
            depth += value
        else:
            depth -= value
    print(depth * horizontal)
    #part2
    depth, horizontal, aim = 0, 0, 0
    for line in data:
        direction = line[0]
        value = int(line[1])
        if (direction == "forward"):
            horizontal += value
            depth += value * aim
        elif (direction == "down"):
            aim += value
        else:
            aim -= value
    print(depth * horizontal)