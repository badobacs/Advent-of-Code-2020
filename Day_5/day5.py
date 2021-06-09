def get_line(idcard):
    lower = 0
    upper = 127

    for i in range(6):
        half = (upper + lower) // 2
        if idcard[i] == 'F':
            upper = half
        elif idcard[i] == 'B':
            lower = half + 1

    if idcard[6] == 'F':
        return lower
    else:
        return upper

def get_col(idcard):
    upper = 7
    lower = 0

    for i in range(2):
        half = (upper+lower) //2
        if idcard[i] == 'L':
            upper = half
        elif idcard[i] == 'R':
            lower = half + 1
    if idcard[2] == 'L':
        return lower
    else:
        return upper

largest = 0
ids = []
with open('input5.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

    for idcard in data:
        row = get_line(idcard[:7])
        col = get_col(idcard[7:])

        id  = row *8 +  col 
        ids.append(id)
print(max(ids))

for id in ids:
    if id+1 not in ids and id+2 in ids:
        seatid = id+1

print(seatid) 