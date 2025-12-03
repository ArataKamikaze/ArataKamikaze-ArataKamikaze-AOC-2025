sum = 0
try:
    with open('input.txt', 'r') as input:
        for line in input.readlines():
                lineMax = 0
                max1num = 0
                i = 0
                for num in line.strip():
                    if(int(num) >= int(max1num)):
                        max1num = num;
                        for num2 in range(i+1,len(line)):    
                            if(int(num+str(line[num2])) > lineMax):
                                lineMax = int(str(num)+str(line[num2]))
                    i+=1
                print(lineMax)
                sum+=lineMax
except FileNotFoundError:
    print("Error: The file was not found.")
print(sum)
