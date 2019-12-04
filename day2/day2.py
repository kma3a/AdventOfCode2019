import sys

line = open(sys.argv[1],'r').read()

def getInput(string):
    parsedStr = string.strip().split(",")
    return map(int, parsedStr)


def compute(data):
    #input = getInput(data)
    input = data
    i = 0
    getValue = lambda a : input[input[a]]
    while input[i] != 99:
        resultIndex = input[i+3]
        if input[i] == 1:
            input[resultIndex] = getValue(i+1) + getValue(i+2)
        elif input[i] == 2:
            input[resultIndex] = getValue(i+1) * getValue(i+2)
        i += 4
    return input

## TEST 1 addition
line = [1,0,0,0,99]
test1 = compute(line)
print(test1 == [2,0,0,0,99])
print(test1)

## TEST 2 multiplication
line = [2,3,0,3,99]
test2 = compute(line)
print(test2 == [2,3,0,6,99])
print(test2)








