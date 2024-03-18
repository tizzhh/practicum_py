import sys


def determine_index():
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    elem = int(sys.stdin.readline().rstrip())
    if elem in arr:
        return arr.index(elem)

    left, right = 0, len(arr) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(determine_index())
