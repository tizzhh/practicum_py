def find_min_slice_sum(data, elements_in_slice):
    window_sum = sum(data[0:elements_in_slice])
    min_sum = window_sum
    for index in range(elements_in_slice, len(data)):
        window_sum += data[index] - data[index - elements_in_slice]
        min_sum = min(min_sum, window_sum)
    return min_sum


if __name__ == '__main__':
    data = [5, -3, -2, 10, 2, 7, 1, -6, 13]
    elements_in_slice = 4
    print(find_min_slice_sum(data, elements_in_slice))
