with open('input.txt','r') as i:
    lines = i.readlines()

def calcMass(num):
    x = lambda a : a / 3
    return x(num) - 2

def calcSum(array):
    sum = 0
    for item in array:
        number = int(item.strip())
        sum += calcMass(number)
    return sum

#testing calcsum and that we are getting from the input.txt
#print(calcSum(lines) == 34241)

#calcMass tests
#print(calcMass(12) == 2)
#print(calcMass(14) == 2)
#print(calcMass(1969) == 654)
#print(calcMass(100756) == 33583)
