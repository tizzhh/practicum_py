import unittest


class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """
        Возвращает сумму принятых аргументов,
        если аргументов нет, возвращает None.
        """
        if len(args) == 0:
            return None
        return sum(args)


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_summ(self):
        res = self.calc.summ(5, 5)
        exp = 10
        self.assertEqual(res, exp, 'wrong summ for two arg')

    def test_summ_no_argument(self):
        res = self.calc.summ()
        self.assertIsNone(res, 'wrong summ for no arg')

    def test_summ_one_argument(self):
        res = self.calc.summ(5)
        exp = 5
        self.assertEqual(res, exp, 'wrong summ for one arg')
