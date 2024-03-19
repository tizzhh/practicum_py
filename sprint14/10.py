import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:

    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    count = 0
    prev = None
    current = node

    while current and count < idx:
        prev = current
        current = current.next_item
        count += 1

    if current is None:
        return None

    if prev:
        prev.next_item = current.next_item
    else:
        node = node.next_item
    return node


def print_list(node: Node):
    ptr = node
    while ptr is not None:
        print(ptr.value)
        ptr = ptr.next_item


def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3
    # print_list(new_head)


if __name__ == '__main__':
    test()
