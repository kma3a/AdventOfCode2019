import sys


def getInput(string):
    parsedStr = string.strip().split(",")
    return map(int, parsedStr)

def replaceData(array):
    array[1] = 12
    array[2] = 2
    return array


def compute(data):
    if type(data) == str:
        input = getInput(data)
        print("BEFORE")
        print(input)
        input = replaceData(input)
        print("AFTER")
        print(input)
    else:
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

## TEST 3 multiplication
line = [2,4,4,5,99,0]
test3 = compute(line)
print(test3 == [2,4,4,5,99,9801])
print(test3)

## TEST 4 multiplication
line = [1,1,1,4,99,5,6,0,99]
test4 = compute(line)
print(test4 == [30,1,1,4,2,5,6,0,99])
print(test4)

## Actual
line = open(sys.argv[1],'r').read()
real = compute(line)
print(compute(line))










