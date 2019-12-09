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
    hasCharacters = re.search(r'(\d)\1', passString)
    if hasCharacters and hasLength:
        return checkIncrease(passString)
    return False

def checkGroup(password):
    password = str(password)
    numCon = {}
    index = 0
    while index < len(str(password))-1:
        number = password[index]
        if number == password[index+1]:
            numCon[number] += 1
        index += 1
    return numCon


def findPasswordCount(startPoint, endPoint):
    validPasswords = 0
    while startPoint <= endPoint:
        if checkGroup(startPoint) and checkPassword(startPoint):
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

#part 2 tests
print("part 2 tests")
print('it should return true if there are all duplicate numbers')
print(checkGroup(112233))
print(checkGroup(112233) == True)
print('it should return true if there are two sets of doubles')
print(checkGroup(111122) == True)
print(checkGroup(112222) == True)
print('it should return false if there are 3 of the same number')
print(checkGroup(123444) == False)
print('it should return false if there are 3 of the same number in the center')
print(checkGroup(124445) == False)
print('it should return false if there are 4 of the same but does not have another match')
print(checkGroup(122223) == False)
print(checkGroup(222235) == False)
print(checkGroup(222225) == False)




#print(findPasswordCount(235741, 706948))
#441 is not the correct answer
#part 2
# 557 is not right
# 759 is not right Too Low

