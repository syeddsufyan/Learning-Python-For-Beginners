# Decorators


def decor(num): 
    def inner():
        print("IF: Before enhancing Function")
        num()
        print("IF: After Enhancing Function")
    return inner
# @decor
def num():
    print("We will use this function")
    print("and will enhance this in decorator")
result_fun = decor(num)
result_fun()

# another one option

def inner():
    print("IF: Before enhancing Function")
    num()
    print("IF: After Enhancing Function")
    return inner
@decor
def num():
    print("We will use this function")
    print("and will enhance this in decorator")
# result_fun = decor(num)
result_fun()

print('\n\n')
def extract_function_name(func):
    def internal_method(*args, **kwargs):
        print('The method called is:', func.__name__)
        returned_value = func(*args, **kwargs)
        print('The method execution is complete')
        return returned_value
    return internal_method

@extract_function_name
def sum_two_numbers(a,b):
    print("This is called inside the function")
    return a + b


@extract_function_name
def product_two_numbers(a,b):
    print("This is called inside the function")
    return a*b
a,b = 3,4
print('Sum function value:', sum_two_numbers(a,b))
print('Product function value', product_two_numbers(a, b))
 