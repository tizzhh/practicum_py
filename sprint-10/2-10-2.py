def just_plus(first, second):
    try:
        print(first + second)
    except TypeError:
        print('Переданы параметры разного типа!')


first = 5
second = 10
just_plus(first, second)
