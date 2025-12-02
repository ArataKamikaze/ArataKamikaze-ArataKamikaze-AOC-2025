sum = 0
try:
    with open('input.txt', 'r') as input:
        line = input.readline()
        range_list = line.split(',')
        for espaco in range_list:
            start = int(espaco.split('-')[0])
            end = int(espaco.split('-')[1])
            for i in range(start, end+1):
                stringMask = ''
                for j in range(len(str(i))):
                    curr = str(i)[j]
                    stringMask+=curr
                    arraySplit = str(i).split(stringMask)
                    if(all(x == "" for x in arraySplit) and len(arraySplit) > 2):
                        sum+=i
                        print(str(i) + ' - ' + stringMask + ' - yes' +  ' - ' + str(arraySplit))
                        break
                    #else:
                        #print(str(i) + ' - ' + stringMask + ' - no')
                    
                    
                    
except FileNotFoundError:
    print("Error: The file was not found.")
print(sum)