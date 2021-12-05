DIAGRAM_RANGE = 1000

def countLines(diagram):
    counter = 0
    for i in range(DIAGRAM_RANGE):
        for j in range(DIAGRAM_RANGE):
            if(diagram[i][j] > 1):
                counter+=1
    return counter


with open("input5.txt") as file:
    data = [line for line in file.read().split("\n")]
    diagram = [[0 for _ in range (DIAGRAM_RANGE)] for _ in range(DIAGRAM_RANGE)]
    for line in data:
        if(line==""):continue
        line = line.split(" -> ")
        start = line[0].split(",")
        end = line[1].split(",")
        startX, endX = int(start[0]), int(end[0])
        startY, endY = int(start[1]), int(end[1])
        stepX = 1
        stepY = 1
        if(startX > endX):
            stepX = -1
        if(startY > endY):
            stepY = -1
        #straight lines - part 1
        if(startX == endX or startY == endY):
            for i in range(startX, endX+stepX, stepX):
                for j in range(startY, endY+stepY, stepY):
                    diagram[i][j]+=1
        #diagonals - part 2
        else:
            j = startY
            for i in range(startX, endX+stepX, stepX):
                diagram[i][j]+=1
                j+=stepY

    print(countLines(diagram))