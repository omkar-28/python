# l = []
# for i in range(2000,3200+1):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))

# def fac(x):
#     if x == 0:
#         return 1
#     return x * fac(x-1)

# x = int(input("Enter the factorial number: "))
# print(fac(x))

#DIC
x = int(input("Enter the factorial number: "))
dic=dict()
for i in range(1,x+1):
        dic[i]=i*i
print(dic)

values=input()
l=list(values.split(","))
t=tuple(l)
print(l)
print(t)


values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))