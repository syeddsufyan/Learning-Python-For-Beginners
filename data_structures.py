# if
# if-elif-else
# if-else
# nasted if statement
# loops (for) & (for, else)
# loops (while) & (while, else)
# nasted loops

# if
a = 30
b = 20
if a > b:
    print("a greater than b")
    
# if-elif

a = 33
b = 33
if a > b:
    print("a greater than b")
elif a == b:
    print("a and b equal ")
    
a = 33
b = 40
if a > b:
    print("a greater than b")
else:
    print("b greater then a this condition")
   
a = 200
b = 533
if a > b:
    print("a greater than b")
elif a == b:
    print("a equal b")
else:
    print("b greater then a")

# nasted if statement

a = 10
if a > 20:
    print("above ten")
if a == 30:
    print("also above 20")
else:
    print("but no above 20")
    
# one more example 

a = 50
if a > 20:
    print("above ten")
if a > 30:
    print("also above 20")
else:
    print("but no above 20")

# for
fruits = ["apple", "banana", "orange"]
for x in fruits:
    print(x)
for x in "mango":
    print(x)
for x in range(1, 8):
    print(x, end=",")
    
# for else
# complete print for loop then print else
for y in range(6):
    print(y)
else:
    print("End For Loop")

# nasted for loop
adj = ["red", "blue", "while"]
brands = ["levis", "zara", "outfilters"]

for x in adj:
    for y in brands:
        print(x, y)    


# while 
a = 1
while a < 6 :
    print(a)
    a += 1

# control statement (continue , break , pass)
# continue 

z = ["apple", "banana", "mango"]
for x in z:
    if x == "banana":
        continue
    print(x)
    
j = 0
while j < 10 :
    j += 1
    if j == 7:
        continue
    print(j)
    break

for t in range(1,11):
    print(t)
    if (t == 9):
        break

y = 1
z = 10

while y < z:
    print(y)
    if y == 5:
        break
    y += 1
    
# pass     
for x in [8,6]:
    pass
    


x = 'Hello World'
y = {1:'a', 2:'b'}
print('H' in x) 

