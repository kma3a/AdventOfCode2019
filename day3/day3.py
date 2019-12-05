import sys


def parseArg(string):
    return string.strip()

def parseString(string):
    print(string)
    return string.split(',')

def createRow(xIndex):
    print("test")


def drawMap(array, cMap):
    currentPoint = [0,0]
    for command in array:
        movements = int(command[1:])
        if command[0] == 'R':
            cMap[currentPoint[0]] += movements * "-"
            currentPoint[0] += movements
        elif command[0] == 'U':
            if len(cMap[currentPoint[0]]) > currentPoint[1]:
                cMap[currentPoint[0]][currentPoint[1]] = '+'
            else:
                cMap[currentPoint[0]].append('+')
            if len(cMap) < movements - 1:
                print('test')



    return cMap

def computeDistance(data):
    data = map(parseString, data)
    currentMap = [[]]
    return currentMap

## createRowTest
test1 = createRow(5)
print(test1[4] == '|')
print(test1[2] == '*')
print(test1[3] == '*')

## DrawMapTests,
test1= drawMap(['R1'], [[]])
print(len(test1[0]) == 1)
print(test1)

test2= drawMap(['R5'], [[]])
print(len(test2[0]) == 5)
print(test2)

test3= drawMap(['U1'], [[]])
print(test3[0][0] == '+')
print(test3)

test4= drawMap(['U3'], [[]])
print(test4[0][0] == '|')
print(test4[1][0] == '|')
print(test4[2][0] == '+')
print(test4)




## Test 1
line = ['R8,U5,L5,D3','U7,R6,D4,L4']
print(computeDistance(line))



## with argv input
line = open(sys.argv[1],'r').readlines()
line = map(parseArg, line)
print(computeDistance(line))



