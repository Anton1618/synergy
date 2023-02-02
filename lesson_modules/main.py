# Неявный импорт из folder -> __all__ -> *
from folder import *


def decor(func):
    """Декоратор вывода значений"""
    def inner(*args, **kwargs):
        print(' === Декоратор начат === ')
        res = func(*args, **kwargs)
        print(' === Декоратор закончен === ')
        return res
    return inner


@decor
def gl_val():
    """Вывод глобального пространства имен"""
    print(*[i for i in globals().items()], sep='\n')

print(*globals().items(), sep='\n')
# gl_val = decor(gl_val)
# gl_val()


@decor
def find_module(*args):
    """Вывод результата поиска модуля"""
    import sys
    for i in sys.builtin_module_names:
        if i in args:
            print(f" --- Найден модуль {i}! --- ")


# find = find_module('sys', 'math')
# print(find)



