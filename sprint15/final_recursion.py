# id попытки: 111867807

from string import digits

DIGITS = set(digits)


def decode_message(message: str) -> str:
    def inner(pos: int = 0) -> tuple[str, int]:
        res = ''
        multiplier = ''
        while pos < len(message):
            if message[pos] in DIGITS:
                multiplier += message[pos]
            elif message[pos] == '[':
                inner_message, indx_shift = inner(pos + 1)
                res += int(multiplier) * inner_message
                multiplier = ''
                pos = indx_shift
            elif message[pos] == ']':
                break
            else:
                res += message[pos]
            pos += 1
        return res, pos

    return inner()[0]


if __name__ == '__main__':
    message = input()
    print(decode_message(message))
