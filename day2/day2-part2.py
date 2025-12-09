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
            print(z)
            z = str(z)
            halfLength = int(len(z)//2)
            for a in range(1, halfLength+1):
                checkMatch = z[:a]
                print(checkMatch)
                matchLength = len(checkMatch)
                if checkMatch == z[a:a+matchLength]:
                    print("match")
    
#output
#print("Total: " + str(invalidTotal))
