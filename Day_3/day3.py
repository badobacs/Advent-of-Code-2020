with open('input3.txt') as file:
    map = file.readlines()
    map = [line.strip() for line in map]

treeNum = 0
row, col = 0,0

while row+1 < len(map):
    row +=1
    col +=3

    space = map[row][col % len(map[row])]
    if space == '#':
        treeNum +=1

print(treeNum)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

total = 1  

for slope in slopes:
    treeNum = 0
    row, col = 0,0

    while row+1 < len(map):
        row +=slope[1]
        col +=slope[0]

        space = map[row][col % len(map[row])]
        if space == '#':
            treeNum +=1

    total *=treeNum
print(total)