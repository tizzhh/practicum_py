# def choose_person(n: int, k: int) -> int:
#     if k == 1:
#         return n
#     people = list(range(1, n + 1))
#     index = 0
#     while len(people) > 1:
#         index = (index + k - 1) % len(people)
#         people.pop(index)
#     return people[0]


def choose_person_rec(n: int, k: int, people: list[int], index=0) -> int:
    if k == 1:
        return n
    if len(people) <= 1:
        return people[0]
    index = (index + k - 1) % len(people)
    people.pop(index)
    return choose_person_rec(n, k, people, index)


if __name__ == '__main__':
    n, k = int(input()), int(input())
    people = list(range(1, n + 1))
    print(choose_person_rec(n, k, people))
