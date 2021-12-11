def flash(x,y, data):
    if(data[x][y]["val"] > 9 and data[x][y]["flashed"] == False):
        data[x][y]["val"] = 0
        data[x][y]["flashed"] = True
        if(x > 0 and y > 0): 
            if(data[x-1][y-1]["val"]!=0): data[x-1][y-1]["val"]+=1
            flash(x - 1, y - 1, data)
        if(x > 0): 
            if(data[x-1][y]["val"]!=0): data[x-1][y]["val"]+=1
            flash(x - 1, y, data)
        if(x > 0 and y < len(data[0]) - 1): 
            if(data[x-1][y+1]["val"]!=0): data[x-1][y+1]["val"]+=1
            flash(x - 1, y + 1, data)
        if(y > 0): 
            if(data[x][y-1]["val"]!=0): data[x][y - 1]["val"]+=1
            flash(x, y - 1, data)
        if(y < len(data[0]) - 1): 
            if(data[x][y+1]["val"]!=0): data[x][y+1]["val"]+=1
            flash(x, y + 1, data)
        if(x < len(data) - 1 and y > 0):
            if(data[x+1][y-1]["val"]!=0): data[x+1][y-1]["val"]+=1 
            flash(x + 1, y - 1, data)
        if(x < len(data) - 1): 
            if(data[x+1][y]["val"]!=0): data[x+1][y]["val"]+=1
            flash(x + 1, y, data)
        if(x < len(data) - 1  and y < len(data[0]) - 1): 
            if(data[x+1][y+1]["val"]!=0): data[x+1][y+1]["val"]+=1
            flash(x + 1, y + 1, data)



def clearFlashes(data):
    for i in range(x):
        for j in range(y):
            data[i][j]["flashed"] = False

def countFlashes(data):
    counter = 0
    for i in range(x):
        for j in range(y):
            if(data[i][j]["flashed"] == True): counter+=1
    return counter


def findSimulatenousFlash(data):
    for i in range(x):
        for j in range(y):
            if(data[i][j]["val"] != 0): return False
    return True

with open("test11.txt") as file:
    data = [line for line in file.read().split("\n")]
    print(data)
    x = len(data)
    y = len(data[0])
    print(f"x: {x}, y: {y}")
    newData = [[{"val": int(data[j][i]), "flashed": False} for i in range(y)] for j in range(x)]
    #add +1 to all elements
    counter = 0
    for step in range(200):
        for i in range(x):
            for j in range(y):
                newData[i][j]={"val": int(newData[i][j]["val"]) + 1, "flashed": False}
    #check if element will flash
        for i in range(x):
            for j in range(y):
                if(newData[i][j]["val"] > 9):
                    flash(i,j, newData)
        counter += countFlashes(newData)
        clearFlashes(newData)
        #part2
        if(findSimulatenousFlash(newData)): print(step)
    #part1
    print(counter)
    