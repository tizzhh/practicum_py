def is_correct_bracket_seq(par_seq: str) -> bool:
    if not par_seq:
        return True
    stack = []
    par_types = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for par in par_seq:
        if par in par_types.values():
            stack.append(par)
        elif par in par_types:
            if not stack or stack[-1] != par_types[par]:
                return False
            stack.pop()

    return not stack


print(is_correct_bracket_seq(input()))
