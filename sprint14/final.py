# id попытки: 110165766


def min_num_of_platforms(robots_input: list[int], limit: int) -> int:
    min_number = 0
    robots = sorted(robots_input)
    left, right = 0, len(robots) - 1
    while left <= right:
        if robots[left] + robots[right] <= limit:
            left += 1
        min_number += 1
        right -= 1
    return min_number


if __name__ == '__main__':
    robots = [int(num) for num in input().split()]
    limit = int(input())
    print(min_num_of_platforms(robots, limit))
