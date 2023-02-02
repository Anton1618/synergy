from functools import wraps


# === По умолчанию декорируемая функция теряет свои имя и документацию будучи декорированной ===
# def decorator(func):
#     def inner(*args, **kwargs):
#         print('<h1>')  # Открывающий тег заголовка первого уровня
#         res = func(*args, **kwargs)
#         print('</h1>')  # Закрывающий тег заголовка первого уровня
#         return res
#     return inner


# === Ручное присвоение атрибутов декорируемой функции замыканию декоратора ===
# def decorator(func):
#     def inner(*args, **kwargs):
#         print('<h1>')  # Открывающий тег заголовка первого уровня
#         res = func(*args, **kwargs)
#         print('</h1>')  # Закрывающий тег заголовка первого уровня
#         return res
#     inner.__name__ = func.__name__
#     inner.__doc__ = func.__doc__
#     return inner


# === Применение автоматического взятия атрибутов декорируемой функции декоратором wraps модуля functools ===
# def decorator(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print('<h1>')  # Открывающий тег заголовка первого уровня
#         res = func(*args, **kwargs)
#         print('</h1>')  # Закрывающий тег заголовка первого уровня
#         return res
#     return inner


# Декорируемая фукнция
@decorator
def hello(name, surname):
    """ --- Функция печати приветствия --- """
    print(f'Hello, {name} {surname}')


# Вывод информации
print(f'Имя функции: {hello.__name__}')
help(hello)







