import datetime as dt

FORMAT = "%H:%M:%S"
WEIGHT = 75
HEIGHT = 175
K_1 = 0.035
K_2 = 0.029
STEP_M = 0.65

storage_data = {}


def check_correct_data(data):
    if len(data) != 2 or data[0] is None or data[1] is None:
        return False
    return True


def check_correct_time(time):
    if len(storage_data) != 0 and time <= max(storage_data.keys()):
        return False
    return True


def get_step_day(steps):
    return sum(storage_data.values()) + steps


def get_distance(steps):
    return steps * STEP_M / 1000


def get_spent_calories(dist, current_time):
    hours = current_time.hour + current_time.minute / 60
    mean_speed = dist / hours
    spent_calories = (
        (K_1 * WEIGHT + (mean_speed**2 / HEIGHT) * K_2 * WEIGHT) * hours * 60
    )
    return spent_calories


def get_achievement(dist):
    achievement = ""
    if dist >= 6.5:
        achievement = "Отличный результат! Цель достигнута."
    elif dist >= 3.9:
        achievement = "Неплохо! День был продуктивным."
    elif dist >= 2:
        achievement = "Маловато, но завтра наверстаем!"
    else:
        achievement = "Лежать тоже полезно. Главное — участие, а не победа!"
    return achievement


def show_message(time, steps, dist, cal, ach):
    message = f"""\nВремя: {str(time)}.
Количество шагов за сегодня: {steps}.
Дистанция составила {dist:.2f} км.
Вы сожгли {cal:.2f} ккал.
{ach}\n"""
    print(message)


def accept_package(data):
    if not check_correct_data(data):
        return "Некорректный пакет"

    pack_time = dt.datetime.strptime(data[0], FORMAT).time()

    if not check_correct_time(pack_time):
        return "Некорректное значение времени"

    day_steps = get_step_day(data[1])
    dist = get_distance(day_steps)
    spent_calories = get_spent_calories(dist, pack_time)
    achievement = get_achievement(dist)

    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data[pack_time] = day_steps
    return storage_data


package_0 = ("2:00:01", 505)
package_1 = (None, 3211)
package_2 = ("9:36:02", 15000)
package_3 = ("9:36:02", 9000)
package_4 = ("8:01:02", 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
