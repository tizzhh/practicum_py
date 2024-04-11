def sort_by_blueprint(arr: list[int], blueprint: list[int]) -> list[int]:
    res = []
    not_found = []
    for num in blueprint:
        count = arr.count(num)
        if count:
            res += [num] * count

    for elem in arr:
        if elem not in res:
            not_found.append(elem)

    return res + sorted(not_found)


if __name__ == '__main__':
    n = int(input())
    to_sort = [int(num) for num in input().split()]
    m = int(input())
    blueprint = [int(num) for num in input().split()]

    print(*sort_by_blueprint(to_sort, blueprint))
