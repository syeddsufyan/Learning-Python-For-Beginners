def newfunction():
    print("Hello This is function")
newfunction()

def newfunction(name):
    print("Hello it's me " + name)
newfunction("Sufyan")

def newfunction(first_name , last_name):
    print(first_name + last_name)
newfunction("Syed ", "Sufyan")

# set defualt value
def newfunction(country= "America"):
    print("country names" + country)
newfunction("Pakistan")
newfunction("India")
newfunction()
newfunction("Sweden")

def great_persons(*args):
    print("Great Person" + args[2])
great_persons("Azian", "Kashif", "Rafay")

# ** use for key 

def fruits(**kew):
    print("Fruits" + kew['o'])    
fruits(f='Apple', o='Orange' )

def newfunction(fruits):
    for x in fruits:
        print(x)
fruits = ["Banana", "Mango", "Apple"]
newfunction(fruits)

def brands(brands):
        print(brands["z"])
brand = {
    "z" : "zara",
    "l" : "levis"
    }
brands(brand)


# Recursion

# def tri_recursion(k): 
# 	if (k > 0): 
# 		result = k + tri_recursion (k - 1)  
# 		print (result)  
# 	else: 
# 		result = 0  
# 	return result 
 
# print ("\n\nRecursion Example Results") 
# tri_recursion(6) 


def tri_recursion(k): 
	if (k > 0): 
		result = k + tri_recursion (k - 1)  
		print (result)  
	else: 
		result = 0  
	return result 
 
print ("\n\nRecursion Example Results") 
tri_recursion(6) 



def tri_recursion(n): 
	if (n > 0): 
		result = n + tri_recursion (n - 1)  
		print (result)  
	else: 
		result = 0  
	return result 
 
print ("\n\nRecursion Example Results") 
tri_recursion(15) 

# LAMDA FUNCTION

def myfunc(i):
    return lambda a : a * i

x = myfunc(5)
y = x(5)
print(y)


# /--------------Error Exception Handling----------------/

# try-except
division = 0
try:
    value = 20/division
except ZeroDivisionError:
    print("Error")


x =[1,2,3,4]
try:
    value = x[7]
except IndexError:
    print("list Invalid")
    
    
def check_type(year):
    try:
        assert type(year) == int, 'the type of year is not int'
    except:
        print("The Type Of year invalid")
        return False
    return True
        
# check_type(2023.6545) error
check_type(2023) #correct

    
try:
    print(s)
except:
    print("Something Went Wrong")
finally:
    print("The 'Try Except' Is Finish")
    

def returnfunc(x, y):
    c = x + y
    return c
total = returnfunc(10,20)
print(total)