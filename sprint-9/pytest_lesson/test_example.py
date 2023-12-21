# test_example.py
import pytest
from time import sleep

def one_more(x):
    return x + 1


def get_sort_list(str):
    new_list = sorted(str.split(', '))
    return new_list


# @pytest.mark.parametrize(
#     'input_arg, expected_result',  # Названия аргументов, передаваемых в тест.
#     [(4, 5), (3, 5)]  # Список кортежей со значениями аргументов.
# )
# def test_one_more(input_arg, expected_result):  # Те же параметры, что и в декораторе.
@pytest.mark.parametrize(
    'input_arg, expected_result',
    [
        (4, 5), 
        pytest.param(3, 5, marks=pytest.mark.xfail)  # Ожидается падение теста.
    ],
    ids=['First parameter', 'Second parameter',]
)
def test_one_more(input_arg, expected_result):
    assert one_more(input_arg) == expected_result


def test_sort():
    """Тестируем функцию get_sort_list()."""    
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']

@pytest.mark.slow
def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    # Провальный тест:
    # ожидаем число, но вернётся список.
    sleep(3)
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert isinstance(result, int)