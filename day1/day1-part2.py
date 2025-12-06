file = open("input.txt", "r")

password = 0
startingNumber = 50
currentNumber = 0
ignoreFirst = False

#get inputs
for x in file:
    direction = x[0]
    distance = int(x[1:])

    if direction == 'L':
        currentNumber = startingNumber - distance
        if startingNumber == 0:
            ignoreFirst = True
        while currentNumber < 0:
            if currentNumber < 0:
                currentNumber = 100 + currentNumber
                if ignoreFirst == False:
                    password += 1
                ignoreFirst = False
        if currentNumber == 0:
            password += 1

    if direction == 'R':
        currentNumber = startingNumber + distance
        while currentNumber >= 100:
            if currentNumber >= 100:
                currentNumber = currentNumber - 100
                password += 1

    startingNumber = currentNumber

#output
print("The password is: " + str(password))
