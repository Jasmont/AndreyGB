class Car:
    speed, color, name, is_police = None, None, None, False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.__class__.__name__} is riding')

    def stop(self):
        print(f'{self.__class__.__name__} has stopped')

    def turn(self, direction):
        print(f'{self.__class__.__name__} turned {direction}')

    def show_speed(self):
        print(f'Скорость машины: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    town_car = TownCar(79, 'Red', 'Жигули')
    town_car.show_speed()

    sport_car = SportCar(156, 'Silver', 'Tesla')
    sport_car.show_speed()

    work_car = WorkCar(54, 'Blue', 'Kamaz')
    town_car.show_speed()

    police_car = PoliceCar(79, 'White', 'Patriot')
    police_car.show_speed()

    police_car.go()
    police_car.turn('left')
    police_car.turn('right')
    police_car.stop()
