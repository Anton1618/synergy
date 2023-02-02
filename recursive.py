def recursive(value):
    print(value)
    if value < 4:
        recursive(value+1)
    print(value)


recursive(1)
A = 0


F = {
    'C:': {
        "Python39":['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['Readme.txt', "Welcom.html", 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows':{
            'System32': ['acledit.dll', 'actual.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):
    for f in path:
        print(" "*depth, f)                         # Применяется "глубина" отсутпа и выводится элемент ключ словаря
        if type(path[f]) == dict:                   # Если значение f является словарем, то применить рекурсию
            get_files(path[f], depth+1)             # С увеличением глубины на 1
        else:                                       # Иначе объект ялвяется списком
            print(" "*(depth+1), " ".join(path[f])) # Применяется глубина +1 и объединяется список строк директории



# get_files(F, depth=0)