def val_checker(f_lambda):
    """
    "Тащит" функцию в поле переменной декоратора

    :param f_lambda: принес лямбда вырожение
    :return: вернул декорируемую функции
    """
    def inner_func(function):
        """
        "Тащит" декорируемую функцию

        :param function: принес декорируемую функцию
        :return: вернул обертку переменной
        """
        def wrapper(x):
            """
            "Тащит" переменную

            :param x: принес переменную
            :return: вернул результат работы конструкции
            """
            if f_lambda(x) is not True:
                raise ValueError(f'wrong val {x}')

            return function(x)

        return wrapper

    return inner_func


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)
