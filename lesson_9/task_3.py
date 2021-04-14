class Worker:
    name, surname, position, _income = None, None, None, {"wage": 0., "bonus": 0.}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position, wage):
        super().__init__(name, surname, position)
        self._income['wage'] = wage
        self._income['bonus'] = 60. if position is 'Senior' else 40. if position is 'Middle' else 20.

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def get_income(self):
        return self._income['wage'] + (self._income['wage'] * (self._income['bonus'] / 100.))


if __name__ == '__main__':
    emp_1 = Position('Andrey', 'Gribanov', 'Junior', 100000.)
    print(emp_1.get_fullname())
    print(emp_1.get_income())

    emp_2 = Position('Andrey', 'Gribanov', 'Middle', 200000.)
    print(emp_2.get_fullname())
    print(emp_2.get_income())

    emp_3 = Position('Andrey', 'Gribanov', 'Senior', 300000.)
    print(emp_2.get_fullname())
    print(emp_2.get_income())
