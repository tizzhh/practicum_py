class Matr:
    def __init__(self, size, item=None) -> None:
        self.size = size
        self.inner_item = item


def disassemble_matryoshka(matryoshka: Matr):
    if matryoshka.inner_item is None:
        print(
            f'Все матрёшки разобраны! Размер последней матрёшки: {matryoshka.size}'
        )
        return
    print(f'Разобрали матрёшку размера {matryoshka.size}, разбираем дальше!')
    disassemble_matryoshka(matryoshka.inner_item)


if __name__ == '__main__':
    big_matryoshka = Matr('L', Matr('M', Matr('S')))
    disassemble_matryoshka(big_matryoshka)
