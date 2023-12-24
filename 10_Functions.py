# we can write function in 3 different ways

# way 1 simple
def my_simple_func():
    print(5+3)

my_simple_func()

# way 2 by creating variable (simple)
def my_func():
    sum = 5 + 3
    print(sum)

my_func()

# way 3 by passing argument
def argument_func(a , b):
    sum = a + b
    return sum # it return value to function 

sum_res = argument_func(6 , 7)
print(sum_res)