example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    swapped = True
    left, right = 0, len(example_array) - 1
    while swapped:
        swapped = False
        for left in range(0, right):
            if data[left + 1] < data[left]:
                data[left], data[left + 1] = data[left + 1], data[left]
                swapped = True
        right -= 1
    return data


print(bubble_sort(example_array))
