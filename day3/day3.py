import sys


def parseArg(string):
    return string.strip()

def computeDistance(data):
    return data

## Test 1
line = ['R8,U5,L5,D3','U7,R6,D4,L4']
print(computeDistance(line))



## with argv input
line = open(sys.argv[1],'r').readlines()
line = map(parseArg, line)
print(computeDistance(line))



