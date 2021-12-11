with open("input10.txt") as file:
    data = [line for line in file.read().split("\n")]
    newData = data[:]
    bracketsValue = {"}": 1197, "]": 57, ")": 3, ">": 25137}
    incompleteValue = {"}": 3, "]": 2, ")": 1, ">": 4}
    closingBrackets = {"{": "}", "[": "]", "(": ")", "<": ">"}
    stack = []
    invalidChars = []
    for line in data:
        missingChars = []
        firstError = False
        for char in line:
            if(char in "{[(<"):
                stack.append(char)
            else:
                lastChar = stack.pop()
                if(char != closingBrackets[lastChar] and firstError == False):
                    invalidChars.append(char)
                    newData.remove(line)
                    break
    
    #part1
    sum = 0
    for char in invalidChars:
        sum+=bracketsValue[char]
    print(sum)

    #part2
    stack = []
    points = []
    for line in newData:
        sum = 0
        for char in line:
            if(char in "{[(<"):
                stack.append(char)
            else:
                stack.pop()
        while len(stack) > 0:
            lastChar = stack.pop()
            value = incompleteValue[closingBrackets[lastChar]]
            sum = sum * 5 + value
        points.append(sum)
    
    points = sorted(points)
    print(points[len(points) // 2])