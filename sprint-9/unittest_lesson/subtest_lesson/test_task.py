import unittest


def bartender(order):
    if isinstance(order, int) and order > 0:
        return order
    return 'Извините, я не могу вас обслужить!'


class TestBar(unittest.TestCase):

    def test_bartender(self):
        values_results = (
            (5, 5),
            (0, 'Извините, я не могу вас обслужить!'),
            (0.33, 'Извините, я не могу вас обслужить!'),
            (-1.999999, 'Извините, я не могу вас обслужить!'),
            ('askjndas', 'Извините, я не могу вас обслужить!'),
        )

        for value, expected_result in values_results:
            with self.subTest(
                value=value,
                expected_result=expected_result
            ):
                result = bartender(value)
                self.assertEqual(result, expected_result)