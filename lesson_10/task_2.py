from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def count_cloth(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.__V = size

    @property
    def count_cloth(self):
        return self.__V/6.5 + 0.5

    @count_cloth.setter
    def count_cloth(self, value):
        self.__V = value


class Suit(Cloth):
    def __init__(self, height=0.0):
        self.__H = height

    @property
    def count_cloth(self):
        return self.__H * 2 + 0.5

    @count_cloth.setter
    def count_cloth(self, value):
        self.__H = value


if __name__ == '__main__':
    coat = Coat(5)
    print(f'{coat.count_cloth: .2f}')
    coat.count_cloth = 7
    print(f'{coat.count_cloth: .2f}')

    suit = Suit(6)
    print(f'{suit.count_cloth: .2f}')
    suit.count_cloth = 8
    print(f'{suit.count_cloth: .2f}')
