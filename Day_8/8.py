operations = []
with open("input8.txt","r") as file: # file beolvasása
    for line in file.readlines():
        operation = line.split(" ")[0] # hozzátesz egy nullát, ez jelöli hogy hányszor hajtotta végre a kódsort
        offset = int(line.split(" ")[1])
        visits = 0
        operations.append([operation, offset, visits])

# for o in operations:
#     print(o)

accumulator = 0
eip = 0
while eip < len(operations):
    operations[eip][2] += 1 # mindenegyes müveletkor hozzáir a 0-hoz 1-et
    if operations[eip][2] >= 2: #ha kétszer hajtodik végre a müvelet megáll a program
        break
    if operations[eip][0] == "nop":
        eip+=1
    elif operations[eip][0] == "acc":
        accumulator += operations[eip][1]
        eip +=1
    elif operations[eip][0] == "jmp":
        eip += operations[eip][1]


print( "Elso feladatrész megoldása:" + str(accumulator))


# feladat második fele

for operation in operations:            #
    if operation[0] == "jmp":           #átváltja a parancsot egyikröl a másikra
        operation[0] = "nop"
    elif operation[0] == "nop":
        operation[0] = "jmp"
    accumulator = 0                     #
    eip = 0                             #Mindenegyes break után visszállitja az értékeket
    found = True                        #Feltételezem a megoldás valoszinüségét
    for op in operations:               #
        op[2] = 0                       # "látogatás" számát vissza kell állitani nullára
    while eip < len(operations):
        operations[eip][2] +=1
        if operations[eip][2] >= 2:     # 2 vagy annál több alkalomnál megszakitja a hurkot
            found = False
            break
        if operations[eip][0] == "nop":
            eip += 1
        elif operations[eip][0] == "acc":
            accumulator += operations[eip][1]
            eip += 1
        elif operations[eip][0] == "jmp":
            eip += operations[eip][1]
    if operation[0] == "jmp":
        operation[0] = "nop"
    elif operation[0] == "nop":
        operation[0] = "jmp"
    if found == True:
        print("Második Feladatrész megoldás:" + str(accumulator))
