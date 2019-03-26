#basic example of lambda
double= lambda x: x*2
print(double(5))

#Lambda filter list
mylist = [2,20,30,58,103,139,140,15]

result = list(filter(lambda x: (x%2==0),mylist))
print("the number divied by 2 is",result)

#lambda Map function
my_list= [2,20,30,58,103,139,140,15]

new_list=list(map(lambda x: x*3,my_list))
print("the new list is",new_list)
    

#take a list of numbers 
mylist = [12,65,78,34,56,102,339,221]

#use anonymous function
result = list(filter(lambda x: (x % 13 == 0 ), mylist))

print("the NUmber divided by 13 are",result)

#Print power to 2 ussing lambda function
terms = int(input("How many terms? "))

result = list(map(lambda x: 2 ** x, range(terms)))
print("The total terms is:",terms)
for i in range(terms):
    print("2 raised to power of", i,"is",result[i])

