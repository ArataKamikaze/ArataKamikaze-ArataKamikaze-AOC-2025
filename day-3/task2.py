sum = 0
length = 2

def getMaxNum(string, min, max):
    maxNum = 0
    pos = min
    i = min
    oldString = string
    
    if max == 0:
        max = None
    string = string[min:max]
    for num in string:
        if(int(num)> maxNum):
            maxNum = int(num)
            pos = i
        i+=1
    return maxNum, pos+1

try:
    with open('input.txt', 'r') as input:
        for line in input.readlines():
            numStr = ''
            min = 0
            max = length-1
            j = 0
            for pos in range(length):
                maxNum, min = getMaxNum(line.strip(), min, max*-1)
                max = length-1-pos-1
                numStr+=str(maxNum)
            sum+= int(numStr)                    
except FileNotFoundError:
    print("Error: The file was not found.")
print(sum)
