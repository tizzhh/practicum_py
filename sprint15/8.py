def correct_merge(arr: list[int]) -> bool:
    if len(arr) == 1 or not arr:
        return True
    arr = sorted(arr)
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - prev > 1:
            return False
        prev = arr[i]
    return True


def max_number_of_blocks(arr: list[int]) -> int:
    num_of_blocks = 0
    elem_to_found = 0
    left, right = 0, 0
    while right < len(arr):
        while right < len(arr) and arr[right] != elem_to_found:
            right += 1
        while right < len(arr) and not correct_merge(arr[left : right + 1]):
            right += 1
        elem_to_found = max(arr[left : right + 1]) + 1
        right += 1
        left = right
        num_of_blocks += 1

    return num_of_blocks if num_of_blocks else 1


if __name__ == '__main__':
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(max_number_of_blocks(arr))
