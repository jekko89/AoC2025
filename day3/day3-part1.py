file = open("input.txt", "r")

total = 0

#inputs
for bank in file:
    bank = bank.strip()
    bankLength = len(bank)
    firstLargest = 0
    firstLargestIndex = 0
    secondLargest = 0
    
    #Get first largest number. Do not include last number.
    for volt in bank[:bankLength-1]:
        volt = int(volt)
        if volt > firstLargest:
            firstLargest = volt
            firstLargestIndex = bank.index(str(volt))
    
    #Get remaining numbers after first largest number and find largest.
    remainingBank = bank[firstLargestIndex+1:]
    for secondVolt in remainingBank:
        secondVolt = int(secondVolt)
        if secondVolt > secondLargest:
            secondLargest = secondVolt

    #Add to running total
    total += int(firstLargest) * 10 + int(secondLargest)
    
#output
print(total)
