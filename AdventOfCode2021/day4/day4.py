def checkBingoWin(dict, board):
    #check rows
    rowCheck, columnCheck = False, False
    for i in range(5):
        rowCheck = True
        row = board[5*i:5*i+5]
        for number in row:
            if(dict[number]!=1):
                rowCheck = False
        if(rowCheck):
            return True 
    #check columns
    for i in range(5):
        columnCheck = True
        column = board[i::5]
        for number in column:
            if(dict[number]!=1):
                columnCheck = False
        if(columnCheck):
            return True 

def sumUnvisitedElements(board):
    return sum(int(key) if board[key] == 0 else 0 for key in board.keys())

def fastestBoard(boardResult):
    fastest = boardResult[0][2]
    fastestIdx = 0
    for idx, br in enumerate(boardResult):
        if(br[2] < fastest):
            fastest = br[2]
            fastestIdx = idx
    return boardResult[fastestIdx]

def slowestBoard(boardResult):
    slowest = boardResult[0][2]
    slowestIdx = 0
    for idx, br in enumerate(boardResult):
        if(br[2] > slowest):
            slowest = br[2]
            slowestIdx = idx
    return boardResult[slowestIdx]


with open("input4.txt") as file:
    data = [line for line in file.read().split("\n\n")]
    numbers = data[0].split(",")
    boards = data[1:]
    boardResult = []
    for board in boards:
        boardElements = board.split()
        boardDictionary = {x: 0 for x in boardElements}
        countNumbers = 0
        for number in numbers:
            countNumbers +=1
            if (number in boardDictionary.keys()):
                boardDictionary[number] = 1
            if(checkBingoWin(boardDictionary, boardElements)):
                x = sumUnvisitedElements(boardDictionary)
                boardResult.append([number, x * int(number), countNumbers])
                break
    print(boardResult)
    #part1
    print(fastestBoard(boardResult)[1])
    #part2
    print(slowestBoard(boardResult)[1])