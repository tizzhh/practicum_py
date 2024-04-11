wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]
my_ticket = 9314543


def binary_search(arr, x, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, x, left, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, right)


index = binary_search(wins, my_ticket, 0, len(wins) - 1)
print(index)
