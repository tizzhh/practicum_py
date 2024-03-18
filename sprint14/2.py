import sys


def delete_duplicates():
    arr_len = int(sys.stdin.readline().rstrip())
    unique_vals = set(map(int, sys.stdin.readline().rstrip().split()))
    print(*(sorted(unique_vals) + ['_'] * (arr_len - len(unique_vals))))


if __name__ == '__main__':
    delete_duplicates()
