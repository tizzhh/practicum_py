# id попытки: 111880775


from string import digits

DIGITS = set(digits)


def decode_message(message: str) -> str:
    stack: list[tuple[str, str]] = []
    multiplier = ''
    res = ''
    for char in message:
        if char in DIGITS:
            multiplier += char
        elif char == '[':
            stack.append((res, multiplier))
            multiplier = ''
            res = ''
        elif char == ']':
            inner_message, num = stack.pop()
            res = inner_message + res * int(num)
        else:
            res += char
    return res


if __name__ == '__main__':
    message = input()
    print(decode_message(message))
