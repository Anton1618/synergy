#!C:\python\python
def decorator(func):
    def inner(*args):
        print()
        print(f" --- Start decorator --- ")
        res = func(*args)
        print(f"Результат {func.__name__}: {res}")
        print(f" --- Finish decorator --- ")
        print()
    inner.__doc__ = func.__doc__
    inner.__name__ = func.__name__
    return inner


@decorator
def say():
    """Возвращает переданную строку"""
    res = input("Введите текст для печати: ")
    return res


@decorator
def matrix_gen():
    """Создает матрицу по переданным значениям"""
    from random import randint
    N = int(input("Введите количество строк: "))
    M = int(input("Введите количество столбцов: "))
    matrix = []
    for i in range(N):
        row = []
        for i in range(M):
            n = randint(-99, 99)
            row.append(n)
        matrix.append(row)
    for i in matrix:
        for j in i:
            print("%4d" %j, end="")
        print()
    return matrix 


@decorator
def mul():
    """Умножает два переданных значения"""
    a, b = [int(input(f"Введите значение элемента {i+1} для умножения: ")) for i in range(2)]
    return a * b


def menu():
    while (command := input(f"""
        Доступные программы
        say - {say.__doc__}
        matrix_gen - {matrix_gen.__doc__}
        mul - {mul.__doc__}
        mat_print - {mat_print.__doc__}
        stop - для завершения сеанса
        Введите название программы: """
        )) != 'stop':
            if command in globals():
                globals()[command]()

menu()
