def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам.
    result = ''
    for i in incoming:
        result += str(i)
    return result


# Первое тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из целых и дробных чисел.

mixed_numbers = [1, 1.5]
result_numbers = '11.5'

# Вместо многоточия напишите утверждение, которое должно быть проверено.
assert (
    series_sum(mixed_numbers) == result_numbers
), 'Функция series_sum() некорректно обрабатывает смешанный список из int и float.'

# Второе тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из чисел и строк.

mixed_numbers_strings = [1, 'a']
result_numbers_strings = '1a'

# Вместо многоточия напишите утверждение, которое должно быть проверено.
assert (
    series_sum(mixed_numbers_strings) == result_numbers_strings
), 'Функция series_sum() некорректно обрабатывает смешанный список из чисел и строк.'

# Третье тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать пустой список.
empty = []
result_empty = ''

# Вместо многоточия напишите утверждение, которое должно быть проверено.
assert (
    series_sum(empty) == result_empty
), 'Функция series_sum() некорректно обрабатывает пустой список'


class Contact:
    def __init__(self, name, year_birth, is_programmer):
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return (
            f'{self.name}, '
            f'возраст: {self.age_define()}, '
            f'статус: {self.programmer_define()}'
        )


# Создайте экземпляр класса Contact с необходимыми параметрами.
# Например, test_old_none_programmer = Contact('Пушкин', 1799, False).
test_old_none_programmer = Contact('Пушкин', 1799, False)
# Напишите assert и в нём проверьте,
# что метод programmer_define() этого экземпляра возвращает строку "Нормальный".
# Во втором assert проверьте, возвращает ли метод age_define() значение "Старейшина".
expected_string = 'Нормальный'
assert (
    test_old_none_programmer.programmer_define() == expected_string
), 'Метод programmer_define неправильно присваивает статус'

expected_age = 'Старейшина'
assert (
    test_old_none_programmer.age_define() == expected_age
), 'Метод age_define неправильно опрделеяет возраст'

test_young_yes_programmer = Contact('Абоба', 2000, True)

expected_string = 'Программист'
assert (
    test_young_yes_programmer.programmer_define() == expected_string
), 'Метод programmer_define неправильно присваивает статус'

expected_age = 'Молодой'
assert (
    test_young_yes_programmer.age_define() == expected_age
), 'Метод age_define неправильно опрделеяет возраст'

test_mid_yes_programmer = Contact('Абоба', 1970, True)

expected_age = 'Олдскул'
assert (
    test_mid_yes_programmer.age_define() == expected_age
), 'Метод age_define неправильно опрделеяет возраст'
