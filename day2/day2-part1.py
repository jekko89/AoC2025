file = open("input.txt", "r")

invalidTotal = 0

#get inputs
for x in file:
    prodIds = x.split(",")
    for y in prodIds:
        y = y.split("-")
        start = int(y[0])
        end = int(y[1])
        for z in range(start, end+1):
            z = str(z)
            length = int(len(z)//2)
            firstHalf = z[:length]
            secondHalf = z[length:]
            if firstHalf == secondHalf:
                invalidTotal += int(z)
    
#output
print("Total: " + str(invalidTotal))
