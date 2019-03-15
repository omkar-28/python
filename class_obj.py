# class parrot(object):
#     species = "bird"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sing(self,song):
#         return "{} sing {}".format(self.name, song)

#     def dance(self):
#         return "{} is dancing".format(self.name)
# blu = parrot("Blu",10)
# woo = parrot("Woo",12)

# print(blu.sing("Hello"))
# print(woo.dance())

# print("{} is a {}".format(blu.name,blu.__class__.species))
# print("{} is {} years old".format(blu.name,blu.age))


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

a = Polygon(4)
a.inputSides()
a.dispSides()
class triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c=self.sides

        s= (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)


c = triangle()
c.inputSides()
c.dispSides()
c.findArea()