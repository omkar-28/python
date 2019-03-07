#take a list of numbers 
mylist = [12,65,78,34,56,102,339,221]

#use anonymous function
result = list(filter(lambda x: (x % 13 == 0 ), mylist))

print("the NUmber divided by 13 are",result)