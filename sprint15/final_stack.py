# id попытки: 111869603


from string import digits

DIGITS = set(digits)


def decode_message(message: str) -> str:
    stack = []
    multiplier = ''
    res = ''
    for ch in message:
        if ch in DIGITS:
            multiplier += ch
        elif ch == '[':
            stack.append((res, multiplier))
            multiplier = ''
            res = ''
        elif ch == ']':
            inner_message, num = stack.pop()
            res = inner_message + res * int(num)
        else:
            res += ch
    return res


if __name__ == '__main__':
    message = input()
    print(decode_message(message))
