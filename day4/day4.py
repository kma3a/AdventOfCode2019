import re

def checkIncrease(string):
    isIncreasing = True
    index = 0
    while isIncreasing and index < len(string)-1:
        isIncreasing = string[index] <= string[index + 1]
        index += 1
    return isIncreasing

#checks for all but within range
def checkPassword(password):
    passString = str(password)
    #checkes password length is 6
    hasLength = len(passString) == 6
    #check for double characters
    hasCharacters = re.findall(r'(\d)\1', passString)
    if hasCharacters and hasLength:
        return checkIncrease(passString)
    return False

def findPasswordCount(startPoint, endPoint):
    validPasswords = 0
    while startPoint <= endPoint:
        if checkPassword(startPoint):
            validPasswords += 1
        startPoint += 1
    return validPasswords

#checkIncrease tests
print('checkIncrease')
print('it returns true if it increases')
print(checkIncrease('123') == True)
print('it returns false if does not increase')
print(checkIncrease('634') == False)
print('it returns false if the las character does not increase')
print(checkIncrease('664') == False)
print('it returns true if remains the same')
print(checkIncrease('222') == True)
print(checkIncrease('225') == True)

#check Password tests
print('checkPassword')
print('it returns true if valid password')
print('it only has the same number')
print(checkPassword(111111) == True)
print('it has some increase at the end')
print(checkPassword(111123) == True)
print(checkPassword(111123) == True)
print('returns true if the increase is in the middle')
print(checkPassword(123445) == True)
print('it returns false if invalid password')
print('it has does not increase')
print(checkPassword(223450) == False)
print(checkPassword(232450) == False)
print('it has no doubles')
print(checkPassword(123789) == False)


print(findPasswordCount(235741, 706948))
#441 is not the correct answer
