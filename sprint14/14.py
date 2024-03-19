def find_two_indexes(data, expected_sum):
    # Ваше решение?
    for i, elem1 in enumerate(data):
        for j, elem2 in enumerate(data):
            if i != j and elem1 + elem2 == expected_sum:
                return (i, j)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
