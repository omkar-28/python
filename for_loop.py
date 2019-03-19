# total = 0
# for i in range(0,10):
#     print("hello : {}".format(i))
#     total += i
# print("The sum is", end=" ")
# print(total)

# # USer Input for Loop
# sum = 0
# num = int(input("Enter the number: "))
# for i in range(1,num+1):
#     print(i)
#     sum += i
# print(sum)

# #Sum using the string input
# num = input("Enter the number: ")
# total = 0

# for i in range(0,len(num)):
#     total += int(num[i])
# print(total)

#Count the number of characters
name = input("Enter the name: ")
temp_var=""
for i in range(0,len(name)):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f'{name[i]} : {name.count(name[i])}')