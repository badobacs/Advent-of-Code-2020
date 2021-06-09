fields = ['byr', 'iyr', 'eyr', 'hgt','hcl', 'ecl', 'pid']
validEntryCard = []

def is_valid_entry_card(ec):
    for field in fields:
        if field not in ec:
            return False
    return True




with open('input.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data]

validCount = 0

currentEntryCard = ''
for line in data:
    if line != '':
        currentEntryCard += ' ' + line
    else:
        if is_valid_entry_card(currentEntryCard):
            validEntryCard.append(currentEntryCard)
            
            validCount +=1
        currentEntryCard = ''

if  is_valid_entry_card(currentEntryCard):
    validEntryCard.append(currentEntryCard)
    validCount += 1
print(validCount)

# 2. rész

def valid_byr(byr):
    byr = int(byr)
    if byr < 1920 or byr > 2002:
        return False
    return True

def valid_iyr(iyr):
    iyr = int(iyr)
    if iyr < 2010 or iyr > 2020:
        return False
    return True 
def valid_eyr(eyr):
    eyr = int(eyr)
    if eyr < 2020 or eyr > 2030:
        return False
    return True
def valid_hgt(hgt):
    units = hgt[-2:]

    if units not in ['in', 'cm']:
        return False

    hgt = int(hgt[:-2])
    if units =='in':
        if hgt < 59 or hgt > 76:
            return False
    elif units == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    return True


def valid_hcl(hcl):
    if hcl[0] != '#': return False
    if len (hcl[1:]) !=6:
        return False
    return True

def valid_ecl(ecl):
    colors = ['grn','blu','brn','hzl','oth','amb','gry']
    if ecl not in colors:
        return False
    return True

def valid_pid(pid):
    if len (pid) != 9:
        return False
    return True

def is_valid_data(entrycard):
    entrycard = entrycard.split()
    data = {}

    for item in entrycard:
        key = item[:3]
        value = item[4:]
        data[key] = value
    if not valid_byr(data['byr']):
        return False
    
    if not valid_iyr(data['iyr']):
        return False
    if not valid_eyr(data['eyr']):
        return False
    if not valid_hgt(data['hgt']):
        return False
    if not valid_hcl(data['hcl']):
        return False
    if not valid_ecl(data['ecl']):
        return False
    if not valid_pid(data['pid']):
        return False
    return True

validCount = 0   
for ec in validEntryCard:
    if is_valid_data(ec):
        validCount +=1


print(validCount)


