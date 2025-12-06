file = open("input.txt", "r")

#set values
password = 0
currentNumber = 50

#get inputs
for x in file:
    direction = x[0]
    distance = int(x[1:])

    if direction == 'L':
        currentNumber -= distance
        while currentNumber < 0:
            currentNumber = 100 + currentNumber

    if direction == 'R':
        currentNumber += distance
        while currentNumber >= 100:
            currentNumber = currentNumber - 100

    if currentNumber == 0:
        password += 1
    
#output
print("The password is: " + str(password))
