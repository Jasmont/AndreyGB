class Cell:
    ERROR_MESSAGE = 'Please pass \'Cell\' class object!'

    def __init__(self, partition: int):
        self.partition = partition

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(self.ERROR_MESSAGE)

        return Cell(self.partition + other.partition)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(self.ERROR_MESSAGE)

        result = self.partition - other.partition

        if result <= 0:
            raise ValueError('Can\'t subtract these cells!')

        return Cell(result)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(self.ERROR_MESSAGE)

        return Cell(self.partition * other.partition)

    def __floordiv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(self.ERROR_MESSAGE)

        return Cell(int(self.partition // other.partition))

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(self.ERROR_MESSAGE)

        return Cell(int(self.partition / other.partition))

    def make_order(self, row):
        st = ''

        for i in range(1, self.partition + 1):
            st += '*\n' if i % row == 0 else '*'

        return st


if __name__ == '__main__':
    cell_1 = Cell(7)
    cell_1 += Cell(8)
    cell_1 /= Cell(5)
    cell_1 *= Cell(5)
    cell_1 //= Cell(5)
    cell_1 *= Cell(3)

    print(cell_1.partition)

    print(cell_1.make_order(5))
