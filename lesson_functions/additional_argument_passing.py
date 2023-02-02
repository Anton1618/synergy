import math


# Декоратор производной функции
# def decorator(func):
#     def inner(x, *args, **kwargs):
#         dx = 0.01
#         res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#         return res
#     return inner


# Для возможности передачи аргумента точности декоратору
def df_decorator(dx=0.01):
    def decorator(func):
        def inner(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        return inner
    return decorator



#@decorator  # Декоратор без возможности передачи аргумента
@df_decorator(0.0000001)  # Декоратор с возможностью передачи аргумента
def sin_df(x):
    return math.sin(x)


print(sin_df(math.pi/3))
