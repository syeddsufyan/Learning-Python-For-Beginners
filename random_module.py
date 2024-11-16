import random
a = random.randint(2,8)
print(a)

p1 = random.randrange(2,4)
print(p1)

l = [10,20,30.50,60]
lc = random.choice(l)
print(lc)

r = random.random()
print(r)

l = [10,20,30]
random.shuffle(l)
print(l)

u = random.uniform(2,8)
print(u)
