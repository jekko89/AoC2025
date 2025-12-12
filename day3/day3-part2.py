file = open("input.txt", "r")

total = 0

#inputs
for bank in file:
    bank = bank.strip()
    nextLargestIndex = 0
    joltage = ""
    
    for x in reversed(range(12)):
        nextHighest = 0
        end = len(bank) - x
        for volt in bank[nextLargestIndex:end]:
            volt = int(volt)
            if volt > nextHighest:
                nextHighest = volt
        joltage += str(nextHighest)
        nextLargestIndex = bank.find(str(nextHighest), nextLargestIndex) + 1

    total += int(joltage)

#output

print(total)
