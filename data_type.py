# Mutable object can be change 
# Immutable object cannot be change

# Mutable 
# list 
# dictionary 
# bytearray
# set

# Immutable
# int
# float
# complex
# string
# tuple
# --------
# More
# range
# frozenset
# bool
# bytes

# =============================================================================
# str (text type)
print("Hello World")
print('Hello World')

# assign string to a var
a = "Hello Bro"
print(a)

# multiline string
# first method
j = "some times you need to store some \
text spread multiple lines"
print(j)
# second method
y = """some times you need to store some 
text spread multiple lines"""
print(j)

# numaric type (int, float, complex)
x = 1 # int
y = 2.8 # float
z = 1j # comlpex
print(x, type(x))
print(y, type(y))
print(z, type(z))

# sequence type (list, range, tuple)
# language = "python"
# python indexing
#  p = [0] , -6
#  y = [1] , -5
#  t = [2] , -4
#  h = [3] , -3
#  o = [4] , -2
#  n = [5] , -1

# list

# always print with index number
thislist = ["apple", "banana", "mango"]
print(thislist[0])
print(type(thislist))
# negative indexing
print(thislist[-1])
# range
thisrange = ["apple", "banana", "mango", "cherry", "orange"]
print(thisrange[2:4]) #starting 2 including 2 or one index before 5 end

# tuple

# eligible use function in tuple
# min
# max
# count
# index
# sum
# if add in sum value 10 write this print(sum, 10) imagine output 20

thistuple = ("apple", "banana", "mango", "cherry", "orange")
print(thistuple[4])
print(type(thistuple))

# dict (mapping type)

# depend on keys not index
thisdict ={
        "brand":  "zara",
        "fruit":  "cheery",
        "year":  2023
    
    }
print(thisdict)
print(thisdict["brand"])

# set fronzenset (set type)
# set

thisset = {"apple", "banana", "orange"}
print(thisset)
# one item add using (add) method
thisset.add("mango") 
print(thisset)
# multipule item add using update method
thisset.update(["cheery", "grapes"])
print(thisset)
# find set qty using len(
print(len(thisset))
thisset.remove("banana")
thisset.discard("cheery")
print(thisset)
print(type(thisset))

# frozenset
# as same set but not add & remove & update frozenset that is diffrence

city = frozenset(["karachi", "lahore"])
print(city)


# bool (boolan type)

print(10 > 9)
print(10 == 9)
print(10 < 9)
print(10 != 9)
print(type(10 > 9))

a = 20
b = 10
if b > a:
    print("b is greater than a")
else:
    print("b is not greater then a")
    
# Python Dates (don't foget to import datetime)
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
y = datetime.datetime.now() #current datetime
year = x.strftime("%Y")
month = x.strftime("%m")
day = x.strftime("%d")
print("Year:", year) 
print("Month:", month) 
print("Day:", day) 
time = x.strftime("%H:%M:%S")
print("Time:", time)
date_time = x.strftime("%m|%d|%Y, %H:%M:%S")
print("Date Time:", date_time)
print(datetime.datetime(2023,2,12))
from datetime import datetime
now = datetime.now()
z = now.strftime("%H:|%M:|%S")
print(z)
d = now.strftime("%A:|%B:|%Y")
print(d)
# calculating time and mo week month duration
import datetime
from datetime import timedelta
t1 = timedelta(weeks = 4, days = 5, hours = 2, minutes = 8, seconds = 9 )
t2 = timedelta(weeks = 7, days = 2, hours = 6, minutes = 3, seconds = 1 )
print(t1)
print(t2)
t3 = t1 - t2
print(t3)