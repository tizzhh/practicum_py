import pytest  # Для использования маркеров нужно импортировать модуль pytest.

# pytestmark = pytest.mark.skip  # Все тесты в этом файле будут пропущены.


@pytest.mark.skip  # Тест с этим маркером будет пропущен.
def test_will_be_skipped():
    assert True


def test_will_be_launched():
    assert False


old_version = True


@pytest.mark.xfail(
    "sys.version_info < (2, 1)",
    reason='Это старая версия Python, чего же вы ждали!',
)
def test_for_new_python():
    assert old_version == True


@pytest.mark.xfail(reason='Пусть пока падает, завтра починю.')
def test_false():
    assert False
