def list_superset(list_set_1, list_set_2):
    if sorted(list_set_1) == sorted(list_set_2):
        return 'Наборы равны.'
    count = 0
    if len(list_set_2) < len(list_set_1):
        for elem in list_set_2:
            if elem not in list_set_1:
                return 'Супермножество не обнаружено.'
        return f'Набор {list_set_1} - супермножество.'
    else:
        for elem in list_set_1:
            if elem not in list_set_2:
                return 'Супермножество не обнаружено.'
        return f'Набор {list_set_2} - супермножество.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
