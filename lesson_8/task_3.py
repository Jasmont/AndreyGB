def type_logger(func):
    def inner_func(*args):
        results = [f'{func(i)[0]}: {type(i)}' for i in args]
        return f'{func.__name__}({", ".join(results)})'
    return inner_func


@type_logger
def calc_cube(*args):
    return [i ** 3 for i in args]


if __name__ == '__main__':
    a = calc_cube(5, 6)
    print(a)
