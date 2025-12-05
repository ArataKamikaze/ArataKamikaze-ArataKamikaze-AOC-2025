import sys
dial = 50
old_dial = dial
counter = 0
i = 0
try:
    with open('dayOne.txt', 'r') as input:
        for line in input.readlines():
            i+=1
            old_dial = dial
            # grabs the values
            dir = line[0]
            value = int(line[1:].strip())
            
            #check for values over 99
            if(value > 99):
                counter += value // 100
                value = value % 100
            
            if dir == 'L':
                fpos = dial
                dial -= value
                spos = dial
                if fpos > 0 and spos < 0 :
                    counter += 1
                
                if(dial < 0):
                    dial = 100 + dial
            elif dir == 'R':
                fpos = dial
                dial += value
                spos = dial
                if spos > 100 :
                    counter += 1
                if(dial > 99):
                    dial = dial - 100
            else:
                print("Error: Invalid direction.")
                break
            if(dial == 0):
                counter +=1
                
            print(str(i) + ' - ' + str(old_dial) + ' - ' + str(line.strip()) + ' - ' + dir + ' - ' + str(value) + ' - ' + str(dial))
except FileNotFoundError:
    print("Error: The file was not found.")
print(counter)
