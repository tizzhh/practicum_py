import unittest


class Calculator:
    """Производит арифметические действия."""

    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        if num2 == 0:
            raise ZeroDivisionError('Не могу делить на ноль')
        return num1 / num2


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    # Подготовьте данные для теста при помощи фикстур.
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_divider(self):
        act = self.calc.divider(5, 1)
        self.assertEqual(act, 5, 'текст, если проверка провалена')

    def test_divider_zero_division(self):
        # Проверьте, что деление на 0 выбрасывает исключение
        # with self.assertRaises(
        #     ZeroDivisionError, msg='Zero division'
        # ):
        #     self.calc.divider(5, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divider, 5, 0)
