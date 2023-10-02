from math import sqrt

message: str = (
    'Добро пожаловать в самую лучшую программу для вычисления '
    'квадратного корня из заданного числа'
)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Проверка на отрциательность корня."""
    if your_number <= 0:
        return

    sqrt: float = calculate_square_root(your_number)
    print(
        'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {sqrt}',
    )


print(message)
calc(25.5)
