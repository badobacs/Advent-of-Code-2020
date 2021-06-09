


# f = open("feladat3.txt", "r")
# print(f.read()) 

def get_unique_answer(response):
    questions = []

    for char in response:
        if char not in questions:
            questions.append(char)
    
    return len(questions)

with open('input6.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data]

sum = 0
currentResponse = ''
for line in data:
    if line != '':
        currentResponse += line
    else:
        sum += get_unique_answer(currentResponse)
        currentResponse = ''
sum += get_unique_answer(currentResponse)
 
print("Az elsö feladat megoldása:" + str(sum))

# part2
sum_2 = 0
def get_unique_answer_all(responses):
    question = []
    

    for char in responses[0]:
        inAllLines = True
        for line in responses:
            if char not in line:
                inAllLines = False

        if inAllLines and char not in question:
            question.append(char)
    return len(question)
            

currentResponse = []
for line in data:
    if  line != '':
        currentResponse.append(line)
    else: 
        sum_2 += get_unique_answer_all(currentResponse)
        currentResponse = []
sum_2 += get_unique_answer_all(currentResponse)
print("Az második feladat megoldása:" + str(sum_2))


