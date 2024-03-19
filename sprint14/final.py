# 4 попытка


def min_num_of_platforms(robots: list[int], limit: int) -> None:
    min_number = 0
    robots.sort()
    left, right = 0, len(robots) - 1
    while left <= right:
        if robots[left] + robots[right] <= limit:
            left += 1
        min_number += 1
        right -= 1
    print(min_number)


robots = list(map(int, input().split()))
limit = int(input())
min_num_of_platforms(robots, limit)
