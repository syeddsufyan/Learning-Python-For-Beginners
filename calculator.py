import inspect
import os
testvar = 'Hello'
class Greeter:
    def _init_(self, name):
        self.name = name
    def say_hello(self):
        print('Hello {}!'.format(self.name))
    def say_goodbye(self):
        print('goodbye {}!'.format(self.name))

my_greeter = Greeter()


# func lambda
exp = lambda x : x*x

def show_name_age(first_name:str, last_name:str,age:int):
    print('{} {} is years old'.format(first_name, last_name, age))
    
# inspect.ismodule(os)
# inspect.ismodule(testvar)
inspect.getmembers(my_greeter)
print('\n Inspect ismethod vs. isfunction comparison'.upper())


print('\n Ismethod:\n show_name_age:', inspect.ismethod(show_name_age),
      'exp:', inspect.ismethod(exp),
      'Greeter.say_hello:',
inspect.ismethod(my_greeter.say_hello))

print('\n Isfunction:\n show_name_age:', inspect.isfunction(show_name_age),
      'exp:', inspect.isfunction(exp),
      'Greeter.say_hello:',
inspect.isfunction(my_greeter.say_hello))