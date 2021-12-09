def findBasin(x, y, current, data, basinSymbol):
    if(int(data[x][y]!=9)):newOutputArray[x][y] = basinSymbol
    if(x - 1 >= 0 and int(data[x-1][y]) >  current and int(data[x-1][y]) != 9):
        findBasin(x-1, y, int(data[x-1][y]), data, basinSymbol)
    if(x + 1 < len(data) and int(data[x+1][y]) > current and int(data[x+1][y]) != 9):
        findBasin(x+1, y, int(data[x+1][y]), data, basinSymbol)
    if(y - 1 >= 0 and int(data[x][y-1]) >  current and int(data[x][y-1]) != 9):
        findBasin(x, y - 1, int(data[x][y-1]), data, basinSymbol)
    if(y + 1 < len(data[0]) and int(data[x][y+1]) > current and int(data[x][y+1]) != 9):
        findBasin(x, y + 1, int(data[x][y+1]), data, basinSymbol)

def getBasinLength(x, y, newOutputArray, basinSymbol):
    counter = 0
    for i in range(x):
        for j in range(y):
            if(newOutputArray[i][j] == basinSymbol): counter+=1
    return counter

with open("input9.txt") as file:
    data = [line for line in file.read().split("\n")]
    x = len(data)
    y = len(data[0])
    outputArray = [[-2 for j in range(y)] for i in range(x)]
    newOutputArray = [[110 for j in range(y)] for i in range(x)]
    lowElements = 0
    for i in range(x):
        for j in range(y):
            current = data[i][j]
            [up,down,left,right] = [True, True, True, True]
            #upCondition
            if(i > 0):
                if(data[i-1][j] <= current): up = False
            
            #down condition
            if(i < x - 1):
                if(data[i+1][j] <= current): down = False

            #left condition
            if(j > 0):
                if(data[i][j-1] <= current): left = False
            
            #right condition
            if(j < y - 1):
                if(data[i][j+1] <= current): right = False
            
            if(up and down and left and right): 
                outputArray[i][j] = int(data[i][j])               
                lowElements+=1
    
    #part1
    riskSum = sum(map(sum, outputArray)) + lowElements
    print(lowElements)
    print(riskSum)

    #part2
    basinLengths = []
    for i in range(x):
        for j in range(y):
            if(outputArray[i][j]!=-2):
                findBasin(i,j,int(data[i][j]),data,"b")
                basinLength = getBasinLength(x, y, newOutputArray, "b")
                basinLengths.append(basinLength)
                newOutputArray = [[110 for j in range(y)] for i in range(x)]
    basinLengths = sorted(basinLengths, reverse=True)
    print(basinLengths)
    print(basinLengths[0]*basinLengths[1] * basinLengths[2])
