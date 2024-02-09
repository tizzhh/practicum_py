class LenTooLongError(Exception):
    ...


name = 'ЛилуминАй ЛекатАриба ЛаминачАй Экбат Дэ СэбАт'


def check_name(name):
    if len(name) > 4:
        raise LenTooLongError


check_name(name)
