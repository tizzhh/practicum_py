def longest_max_unique_subst(string: str) -> int:
    if len(string) <= 1:
        return len(string)
    left = 0
    max_len = 0
    chars: dict[str, int] = {}
    for right, char in enumerate(string):
        if char in chars and chars[char] >= left:
            left = chars[char] + 1

        chars[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


print(longest_max_unique_subst(input()))
