file = open("input.txt", "r")

invalidTotal = 0
invalidList = set()

#get inputs
for x in file:
    prodIds = x.split(",")
    for y in prodIds:
        y = y.split("-")
        start = int(y[0])
        end = int(y[1])
        for z in range(start, end+1):
            z = str(z)
            string_length = len(z)
            for a in range(1, string_length // 2 + 1):
                candidate_length = a
                candidate = z[0:candidate_length]
                candidate_count = z.count(candidate)
                if candidate_count * candidate_length == string_length and candidate_count > 1:
                    invalidList.add(int(z))
    
#output
for i in invalidList:
    invalidTotal += i
print("Total: " + str(invalidTotal))
