with open('input1.txt') as file:          # file megnyitása
    data = file.readlines()                    #file olvasás
    nums = [ int(line.strip()) for line in data]

# print(nums)
largest = -1

for i in range(len(nums)-1):
     for j in range(i+1, len(nums)):
        num1= nums[i]
        num2 = nums[j]

        if num1+num2 ==2020:
            balance = num1 * num2
            if balance > largest:
                largest = balance

print(largest)

largest = -1

for i in range(len(nums)-2):
     for j in range(i+1, len(nums)-1):
         for k in range(j+1, len(nums)):
             num1, num2, num3 = nums[i], nums[j], nums[k] 
             if num1 +num2+num3 == 2020:
                balance = num1*num2*num3

                if balance > largest:
                    largest = balance

print(largest)
