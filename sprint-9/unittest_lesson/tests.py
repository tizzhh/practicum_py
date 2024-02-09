# tests.py
import unittest
from code import service_100
from datetime import datetime
from time import sleep


class TestTimeService(unittest.TestCase):
    def test_a_time_is_running_out(self):
        first_time = service_100()
        sleep(1)
        second_time = service_100()
        self.assertNotEqual(first_time, second_time)

    def test_b_result_is_datetime(self):
        result = service_100()
        self.assertIsInstance(result, datetime)


# unittest.main()  # Запуск тестов.
