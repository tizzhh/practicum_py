import sys


def valid_mountain_array() -> bool:
    heights = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(heights) < 3:
        return False
    if heights[1] < heights[0]:
        return False
    prev = heights[0]
    going_up = True
    for i in range(1, len(heights)):
        if heights[i] == prev:
            return False
        if going_up:
            if heights[i] < prev:
                going_up = False
        else:
            if heights[i] > prev:
                return False
        prev = heights[i]
    return not going_up


print(valid_mountain_array())
