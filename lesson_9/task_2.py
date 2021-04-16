class Road:
    __length = None
    __width = None

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_asphalt(self, mass, height=1):
        print(f'{self.__length} м*{self.__width} м*{mass} кг*{height} см = {(self.__length * self.__width * mass * height) / 100: .0f} т')


if __name__ == '__main__':
    road_to_create = Road(length=20, width=5000)
    road_to_create.calc_asphalt(25, 5)
