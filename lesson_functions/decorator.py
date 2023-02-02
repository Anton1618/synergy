def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        res = func(*args, **kwargs)
        print('</h1>')
        return res
    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        res = func(*args, **kwargs)
        print('</table>')
        return res
    return inner


@header
@table
def hello(name, surname):
    """ Функция вывода строки """
    print(f"Hello, {name} {surname}")


#hello = table(hello)
hello('Anton', 'Kramskiy')


