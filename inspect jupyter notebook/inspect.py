class Greeter:
    def _init_(self, name):
        self.name = name
    def say_hello(self):
        print('hello {}!'.format(self.name))
    def say_goodbye(self):
        print('goodbye {}!'.format(self.name))

my_greeter = Greeter()
print(id(my_greeter))
print(type(my_greeter))
print(dir(my_greeter))

my_var = 'This is Variable'
print(id(my_var))
print(type(my_var))
print(dir(my_var))

my_num = 453.324
print(id(my_num))
print(type(my_num))
print(dir(my_num))

# --------------- Using This File Jupyter Notebook -----------------------

import inspect
# import os
# testvar = 'Hello'
# class Greeter:
#     def _init_(self, name):
#         self.name = name
#     def say_hello(self):
#         print('Hello {}!'.format(self.name))
#     def say_goodbye(self):
#         print('goodbye {}!'.format(self.name))

# my_greeter = Greeter()


# # func lambda

# exp = lambda x : x*x

# # def show_name_age(first_name:str, last_name:str,age:int):
# #     print('{} {} is years old'.format(first_name, last_name, age))
    
# inspect.getmembers(my_greeter)
# inspect.ismodule(os)
# inspect.ismodule(testvar)
# print('\n Inspect ismethod vs. isfunction comparison'.upper())


# # print('\n Ismethod:\n show_name_age:', inspect.ismethod(show_name_age),
# #       'exp:', inspect.ismethod(exp),
# #       'Greeter.say_hello:',
# # inspect.ismethod(my_greeter.say_hello))

# # print('\n Isfunction:\n show_name_age:', inspect.isfunction(show_name_age),
#       # 'exp:', inspect.isfunction(exp),
#       # 'Greeter.say_hello:',
# # inspect.isfunction(my_greeter.say_hello))

# def show_name_age(first_name:str, last_name:str,age:int):
#     print('{} {} is years old'.format(first_name, last_name, age))
    
# sig = inspect.signature(show_name_age)
# print(sig.parameters)
# print(sig.parameters['first_name'].annotation)