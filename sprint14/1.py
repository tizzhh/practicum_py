import sys


def main():
    num_lines = int(sys.stdin.readline().rstrip())
    output = [None] * num_lines
    for i in range(num_lines):
        output[i] = str(sum(map(int, sys.stdin.readline().rstrip().split())))
    print(*output, sep='\n')


if __name__ == '__main__':
    main()
