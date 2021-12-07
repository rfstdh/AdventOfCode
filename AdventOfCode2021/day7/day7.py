import math

with open("input7.txt") as file:
    data = [int(line) for line in file.read().split(",")]
    fuelCost = math.inf
    for i in range(2000):
        cost = sum([abs(x - i) + sum(range(abs(x-i))) for x in data])
        if(cost < fuelCost):fuelCost = cost
    print(fuelCost)