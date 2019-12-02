def calcMass(num):
    x = lambda a : a / 3
    return x(num) - 2

print(calcMass(12) == 2)
print(calcMass(14) == 2)
print(calcMass(1969) == 654)
print(calcMass(100756) == 33583)
