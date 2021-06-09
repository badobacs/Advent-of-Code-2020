
# f = open("input8.txt", "r")
# print(f.read()) 


with open('input8.txt') as file:          # file megnyitása
    data = file.readlines()                    #file olvasás
    data = [ line.strip() for line in data]

# for line in data:
#     print(line)

def get_acc():
    acc = 0
    line = 0
    instructions = []

    
    # print(currentInstructions)
    while line not in instructions:
        instructions.append(line)
        currentInstructions = data[line]
        currentInstructions = currentInstructions.split()
        cmd = currentInstructions[0]
        num = currentInstructions[1]
        if '+' in num:
            num = int(num[1:])
        else:
            num = int(currentInstructions[1])
        
        if cmd == 'acc':
            acc += num
            line += 1
        elif cmd == 'jmp':
            line += num
        elif cmd == 'nop':
            line += 1
    return acc
acc = get_acc()

# print(acc)

# part 2
def get_acc_eof():

    acc = 0
    line = 0
    instructions = []

    
    # print(currentInstructions)
    while line not in instructions:
        instructions.append(line)
        currentInstructions = data[line]
        currentInstructions = currentInstructions.split()
        cmd = currentInstructions[0]
        num = currentInstructions[1]
        if '+' in num:
            num = int(num[1:])
        else:
            num = int(currentInstructions[1])
        
        if cmd == 'acc':
            acc += num
            line += 1
        elif cmd == 'jmp':
            line += num
        elif cmd == 'nop':
            line += 1
        if line >= len(data):
            return acc, True

    return acc, False



for i in range(len(data)):
    if 'jpm' in data[i]:
        data[i] = data[i].replace('jmp','nop')
        acc, found = get_acc_eof()
        if found:
            print(acc)
            break
        else:
            data[i] = data[i].replace('nop', 'jmp')
            (acc)





     