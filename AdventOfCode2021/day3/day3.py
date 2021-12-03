def countBits(data,lineLength):
    dictionary = {x+1: 0 for x in range(lineLength)}
    for line in data:
        for idx, char in enumerate(line):
            dictionary[idx+1] += int(char)
    return dictionary
    
def keepBitCriteria(data, bitIndex, bitCriteria):
    newData = data[:]
    for line in data:
        if(line[bitIndex]!=bitCriteria):
            newData.remove(line)
    return newData

def getSingleValue(data, isOxygen):
    newData = data[:]
    oxygenIndex = 0
    while len(newData) > 1:
        dictionary = countBits(newData, lineLength)
        if(isOxygen):
            mostCommonBit = "1" if dictionary[oxygenIndex+1] >= (len(newData) / 2) else "0"
        else:
            mostCommonBit = "0" if dictionary[oxygenIndex+1] >= (len(newData) / 2) else "1"
        newData = keepBitCriteria(newData, oxygenIndex, mostCommonBit)
        oxygenIndex+=1
    return newData[0]

with open("input3.txt") as file:
    data = [line for line in file.read().splitlines()]
    dataLength = len(data)
    lineLength = len(data[0])
    #part1
    dictionary = countBits(data, lineLength)
    result = ['1' if value > (dataLength / 2) else '0' for value in dictionary.values()]
    revResult = ['1' if value == '0' else '0' for value in result]
    result = "".join(result)
    revResult = "".join(revResult)
    #convert string to binary number
    print(int(result,2) * int(revResult,2))
    #part2
    # get oxygen 
    oxygenValue = int(getSingleValue(data, True), 2)
    #get co2 
    coValue = int(getSingleValue(data, False), 2)
    print(oxygenValue * coValue)


