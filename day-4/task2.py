sum = 0

try:
    with open('input.txt', 'r') as input:
        lines = [x.strip() for x in input.readlines()]
        while True:
            currSum = 0
            cleanedLines = []
            for lineNum, line in enumerate(lines):
                curPos = 0
                cleanLine = list(line)
                for charPos, char in enumerate(line):
                    surrCount = 5
                    if (char == '@'):
                        surrCount = 0
                        #defines limits
                        minPos = charPos-1 if (charPos > 0) else None
                        maxPos = None if (charPos == len(line)-1) else charPos+2

                        #get workspace on previous line
                        prevLine = []
                        if(lineNum-1 >= 0):
                            prevLine = lines[lineNum-1][minPos:maxPos]
                        
                        #get workspace on next line
                        nextLine = []
                        if(lineNum < len(lines)-1):
                            nextLine = lines[lineNum+1][minPos:maxPos]
                        
                        array = list(prevLine) + list(line[minPos:maxPos]) + list(nextLine)
                        for i in array:
                            if (i == '@'):
                                surrCount+=1
                    if(surrCount < 5):
                        #print(str(lineNum) + '-' + str(charPos))
                        cleanLine[charPos] = '.'
                        currSum+=1
                cleanLineStr = "".join(cleanLine)
                cleanedLines.append(cleanLineStr)
            if(currSum == 0):
                break
            sum+=currSum
            lines = cleanedLines
        [print(x) for x in lines]
except FileNotFoundError:
    print("Error: The file was not found.")
print(sum)
