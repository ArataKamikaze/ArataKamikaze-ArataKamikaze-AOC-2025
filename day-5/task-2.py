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
        #ranges = ranges.sort()
            
        addedRanges = []
        for rangeId, rangevalue in enumerate(sorted(ranges)):
            
            
            start = int(rangevalue.split('-')[0])
            end = int(rangevalue.split('-')[1])
            for rangeId2, rangevalue2 in enumerate(addedRanges):
                start2 = int(rangevalue2.split('-')[0])
                end2 = int(rangevalue2.split('-')[1])        
                
                if(start <= end2 and start >= start2):
                    start = end2+1
                
                if(end >= start2 and end <= end2):
                    end = start2-1
            if(end < start):
                continue
            print(( (end+1) - start))
            sum+=( (end+1) - start)
            addedRanges.append(str(start) + '-' + str(end))
               
except FileNotFoundError:
    print("Error: The file was not found.")
print(sum)