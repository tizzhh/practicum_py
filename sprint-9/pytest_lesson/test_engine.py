# test_engine.py
import pytest

# Импортируем класс двигателя.
from engine_class import Engine


@pytest.fixture
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    return Engine()


# Эта фикстура не возвращает никаких значений, но изменяет объект,
# созданный другой фикстурой.
# @pytest.fixture()
# def start_engine(engine):  # Вызываем фикстуру получения объекта двигателя.
#     """Фикстура запускает двигатель."""
#     # Изменяем значение свойства объекта:
#     engine.is_running = True


@pytest.fixture(
    autouse=True
)  # Обозначаем фикстуру как автоматически вызываемую.
def start_engine(engine):
    """Фикстура запускает двигатель."""
    engine.is_running = True


# def test_engine_is_running(engine, start_engine):  # Вызываем обе фикстуры.
#     """Тест проверяет, работает ли двигатель."""
#     assert engine.is_running  # Проверяем, что значение атрибута is_running это True.

# Добавляем маркер и указываем название фикстуры строкой.
# @pytest.mark.usefixtures('start_engine')
# def test_engine_is_running(engine):  # А из параметров функции фикстуру start_engine убираем.
#     assert engine.is_running


# Вызываем только одну фикстуру.
# Запуск двигателя выполнится автоматически, без вызова.
def test_engine_is_running(engine):
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running
