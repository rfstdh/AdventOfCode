def removeDuplicates(word, replaceChars):
    for char in word:
        if(char in replaceChars):
            word = word.replace(char,"")
    return word

def findEqualStringIndex(testString, stringTable):
    for idx, element in enumerate(stringTable):
        if(sorted(element) == sorted(testString)):
            return str(idx) 
    return 9


def getPatterns(wires, numbersRegexes):
    patterns = {'top': '', "upperRight": '', "lowerRight": '', "upperLeft": '', "lowerLeft": '', "middle": '', "bottom": ''}
    wires = sorted(wires, key=len)
    for wire in wires:
        if(len(wire) == 2):
            patterns['upperRight'] = wire
            patterns['lowerRight'] = wire
            numbersRegexes[1] = wire
        elif(len(wire) == 3):
            patterns['top'] = removeDuplicates(wire, patterns["upperRight"])
            numbersRegexes[7] = wire
        elif(len(wire) == 4):
            patterns['middle'] = removeDuplicates(wire, patterns["upperRight"])
            patterns['upperLeft'] = patterns['middle']
            numbersRegexes[4] = wire
        elif(len(wire) == 7):
            numbersRegexes[8] = wire
    usedChars = patterns["upperRight"] + patterns["middle"] + patterns["top"]
    remainingChars = removeDuplicates("abcdefg", usedChars)
    patterns['bottom'] = remainingChars
    patterns['lowerLeft'] = remainingChars

    return [patterns, numbersRegexes]


def assignNumbers(wires, numbersRegexes, patterns):
    for wire in wires:
        #0,6,9
        if(len(wire) == 6):
            letters = [letter for letter in patterns["lowerLeft"]]
            if wire.count(letters[0]) + wire.count(letters[1]) == 1:
                numbersRegexes[9] = wire
                continue
            letters = [letter for letter in patterns["upperRight"]]
            if wire.count(letters[0]) + wire.count(letters[1]) == 1:
                numbersRegexes[6] = wire
                continue
            numbersRegexes[0] = wire
        #2,3,5
        elif(len(wire)==5):
            letters = [letter for letter in patterns["upperRight"]]
            if wire.count(letters[0]) + wire.count(letters[1]) == 2:
                numbersRegexes[3] = wire
                continue
            letters = [letter for letter in patterns["lowerLeft"]]
            if wire.count(letters[0]) + wire.count(letters[1]) == 2:
                numbersRegexes[2] = wire
                continue
            numbersRegexes[5] = wire
    
    return numbersRegexes

with open("input8.txt") as file:
    data = [line for line in file.read().split("\n")]
    allNumbers = []
    for line in data:
        #data cleaning
        wires = line.split(" | ")[0].split(" ")
        digits = line.split(" | ")[1].split(" ")
        numbersRegexes = ["" for i in range(10)]
        
        #get patterns
        [patterns, numbersRegexes] = getPatterns(wires, numbersRegexes)
        
        #now assign patterns to wires/numbers
        numbersRegexes = assignNumbers(wires, numbersRegexes, patterns)
        
        #final part - converting strign patterns for numbers
        singleNumber = ""
        for digit in digits:
            singleNumber+=findEqualStringIndex(digit, numbersRegexes)
        allNumbers.append(singleNumber) 
    
    #part 1 is just for digit in digits, check length and if its 2,3,4 or 7 add +=1 to counter
    counter = 0
    for line in data:
        digits = line.split(" | ")[1].split(" ")
        for digit in digits:
            if(len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7):
                counter+=1
    print(counter)

    #part 2 output 
    print(sum([int(n) for n in allNumbers]))
            

