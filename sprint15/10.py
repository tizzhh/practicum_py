def num_of_satisfied_customers(
    ordered: list[int], delivered: list[int]
) -> int:
    res = 0
    ordered = sorted(ordered)
    delivered = sorted(delivered)
    or_ptr, del_ptr = 0, 0
    while or_ptr < len(ordered) and del_ptr < len(delivered):
        if delivered[del_ptr] >= ordered[or_ptr]:
            res += 1
            or_ptr += 1
        del_ptr += 1

    return res


if __name__ == '__main__':
    n = int(input())
    ordered = [int(num) for num in input().split()]
    m = int(input())
    delivered = [int(num) for num in input().split()]
    print(num_of_satisfied_customers(ordered, delivered))
