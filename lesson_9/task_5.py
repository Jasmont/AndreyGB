class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.__class__.__name__}: Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.__class__.__name__}: Запуск отрисовки')


class Handle(Stationery):
    def draw(self):
        print(f'{self.__class__.__name__}: Запуск отрисовки')


if __name__ == '__main__':
    pencil = Pencil()
    pencil.draw()

    pen = Pen()
    pen.draw()

    handle = Handle()
    handle.draw()
