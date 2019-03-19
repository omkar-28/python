n = input("enter your number: ")
total = 0
i = 0
while i < len(n):
    total += int(n[i])
    i +=1

print(total)


#count number of letters
name = input("Enter your name: ")
i = 0
dup_letter = ""
while i < len(name):
    if name[i] not in dup_letter:
        dup_letter += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1