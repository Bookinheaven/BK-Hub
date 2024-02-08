def my_func(n):
    return lambda x: x * n

doubler = my_func(2)
print(doubler(5))
