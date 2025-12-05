sum = 0
validList = []
try:
    with open('input.txt', 'r') as input:
        lines = [x.strip() for x in input.readlines()]
        ranges = []
        items = []
        for id, line in enumerate(lines):
            if(line == ''):
                ranges = lines[:id]
                items = lines[id+1:]
                break
        
        for item in items:
            itemInt = int(item)
            for rangeId, rangevalue in enumerate(ranges):
                if(itemInt >= int(rangevalue.split('-')[0]) and itemInt<= int(rangevalue.split('-')[1])):
                    sum+=1
                    break            
               
except FileNotFoundError:
    print("Error: The file was not found.")
print(sum)
