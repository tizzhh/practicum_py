def count_smaller(nums: list[int]) -> None:
    res = []
    for num in nums:
        count = 0
        for num2 in nums:
            if num2 < num:
                count += 1
        res.append(count)
    print(*res)


count_smaller(list(map(int, input().split())))
