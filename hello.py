Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))


def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 1
    print (SwitchExample(argument))

def main():
	#use a for loop over a collection
	Months = ["Jan","Feb","Mar","April","May","June"]
	for i, m in enumerate (Months):
		print((i,m))
		
# use the break and continue statements
		
		
		#for x in range (10,20):
		#if (x == 15): break
		#if (x % 5 == 0) : continue
		#print x


		
if __name__ == "__main__":
	main()
