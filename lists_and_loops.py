#creating a list of numbers and printing them using a loop
list = [2, 9, 5, 16, 10]
for num in list:
    print(num)



#finding the maximum and minimum in a list
list = [11, 9, 12, 16, 10]

min = list[0]
for i in list:
    if i < min:
        min = i    
print(f"The smallest number in the list is {min}")


max = list[0]
for num in list:
    if num > max:
        max = num
print(f"The largest number in the list is: {max} ")



