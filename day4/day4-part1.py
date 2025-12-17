file = open("input.txt", "r")

grid = []
y_count = 0
total = 0

#inputs
for y in file:
    y = y.strip()
    grid.append([])
    for x in y:
        grid[y_count].append(x)
    y_count += 1

#check adjacent
for y_pos in range(len(grid)):
    for x_pos in range(len(grid[y_pos])):
        if(grid[y_pos][x_pos]) == '@':
            rolls = 0
            for x_adj in range(x_pos-1, x_pos+2):
                for y_adj in range(y_pos-1, y_pos+2):
                    try:
                        if grid[y_adj][x_adj] == '@' and (x_pos != x_adj or y_pos != y_adj) and (x_adj > -1 and y_adj > -1):
                            rolls += 1
                    except IndexError:
                        pass
            if rolls < 4:
                total += 1
        
#output
print(total)
