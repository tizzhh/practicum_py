# id попытки: 111880687

from string import digits

DIGITS = set(digits)


def decode_message(message: str) -> str:
    def inner(pos: int = 0) -> tuple[str, int]:
        res = ''
        multiplier = ''
        while pos < len(message):
            cur_char = message[pos]
            pos += 1
            if cur_char in DIGITS:
                multiplier += cur_char
            elif cur_char == '[':
                inner_message, indx_shift = inner(pos)
                res += int(multiplier) * inner_message
                multiplier = ''
                pos = indx_shift
            elif cur_char == ']':
                break
            else:
                res += cur_char
        return res, pos

    return inner()[0]


if __name__ == '__main__':
    message = input()
    print(decode_message(message))
