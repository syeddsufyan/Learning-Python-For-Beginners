class Demo:
    name = "sufyan"
    age = "19"
    live_in = "karachi"

p1 = Demo()
print(p1.name)
print(p1.age)
print(p1.live_in)


class Pak_Country:
    def __init__(self,isb,khi,lhr):
        self.isb=isb
        self.khi=khi
        self.lhr=lhr

country_name = Pak_Country("Islamabad", "Karachi", "Lahore", )
print(country_name.isb)
print(country_name.khi)
print(country_name.lhr)


class Person:
    def __init__(myobject, banana, orange):
        myobject.banana = banana
        myobject.orange = orange
        
    def myfunc(self):
        print("This is " + self.banana)
        
p2 = Person("Banana", "Orange")
print(p2.banana)
print(p2.orange)
p2.myfunc()

class Age:
    def __init__(myobject, age, name):
        myobject.age= age
        myobject.name= name
        
    def myfunc(self):
        print("I'm " + self.age + "Year Old")
        
p3 = Age("19", "Sufyan")
p3.age = 30
p3.name = "syed"
print(p3.age)
print(p3.name)



# delete proporties

class Human:
    def __init__(myobject, sleep, eat):
        myobject.sleep = sleep
        myobject.eat = eat
        
p2 = Human("I wake up early in the morning", "i eat biscuts")
print(p2.sleep)
# del p2.eat

# del objects
# del p2
# print(p2)

# Inheritance (Parent Class, Child Class)
# Parent Class

class Electonic:
    def __init__(self, airport, led):
        self.airport=airport
        self.led=led
    def print_name(self):
        print(self.airport, self.led)
        
p4 = Electonic("aiports 2", "one tweenty inch led")
p4.print_name()
        
# Child Class

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def func(self):
        print(self.x, self.y)
# z = A("abc", "xyz")
# print(z.x)
# print(z.y)
             
class B(A):
    pass
j = B("abc", "xyz")
j.func()
# print(j.x)    
              
        
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def new_func(self):
        print(self.fname, self.lname)
    
    
class Student(Person):
    pass
p5 = Student("Syed", "Sufyan")
p5.new_func()
    

# __init__ function use in child class

class Parents:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def new_func(self):
        print(self.fname, self.lname)
    
    
class Child(Parents):
    def __init__(self, fname, lname):
        Parents.__init__(self, fname, lname)
p5 = Student("Syed", "Usman")
p5.new_func()



    
# super function 

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def new_func(self):
        print(self.fname, self.lname)
    
    
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduation = 2020
p5 = Student("I'm", "Programer Alhamdulillah")
p5.new_func()
print(p5.graduation)


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def new_func(self):
        print(self.fname, self.lname)
    
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation = year
    def func_name_one(self):
        print("I'm", self.fname, self.lname)
p5 = Student("Programer ", "Alhamdulillah", 2020)
# p5.new_func()44
p5.func_name_one()
print(p5.graduation)

# class Fruits:
#     def __init__(self, name, nutrients):
#         try:
#             assert type(nutrients) == list
#         except AssertionError:
#             print("invalid counstraction")
#             raise Exception
#         self.name = name
#         self.nutrients = nutrients
#         self.is_ripe = False
#     def get_name(self):
#         return self.name
#     def get_nutrients(self):
#         print(self.name + 'has following nutrients:')
#         print(value)
#     def check_ripe_function(self):
#         return self.is_ripe
#     def ripe_fruit():
#         self.is_ripe = True

# f = Fruits("Abu Baker", "nutrients is here")
# print(f.get_name())
# f.get_nutrients()
# print(f.check_ripe_function())
# print(ripe_fruit)
    
#  class Name():
#     def __init__(self, b):
#         self.b = b

# def another(a):
#     b = Name(a)
#     return b

# a = another("Karaci")
# print(a.b)   
    
    
    
    
    
        
    

    
    
    
    
    
    
    
    
    