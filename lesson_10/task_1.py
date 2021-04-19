class Matrix:
    def __init__(self, data):
        if not isinstance(data, list) or not any(isinstance(el, list) for el in data):
            raise TypeError('Wrong input type! Expected: list or lists')

        dim = int(sum([len(i) for i in data]) / len(data))
        if not all(len(i) == dim for i in data):
            raise ValueError('Wrong matrix dimensions! All internal matrices should have equal sizes!')

        self.data = data
        self.dims = (len(data), len(data[0]))

    def __str__(self):
        return '\n'.join(' '.join(map(str, i)) for i in self.data)

    def __add__(self, other):
        if not isinstance(other, Matrix) or self.dims != other.dims:
            raise ValueError('Matrices should have equal sizes!')

        result = []

        for i in range(self.dims[0]):
            temp = []
            for j in range(self.dims[1]):
                temp.append(self.data[i][j] + other.data[i][j])
            result.append(temp)

        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = [[31, 22], [37, 43], [51, 86]]
    matrix_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
    matrix_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]

    result_1 = Matrix(matrix_1)
    print(result_1.dims)

    result_2 = Matrix(matrix_2)
    print(result_2.dims)

    result_3 = Matrix(matrix_3)
    print(result_3.dims)

    print('---||---')

    print(result_3)

    print('---||---')

    matrix_4 = Matrix([[1, 2], [3, 4], [5, 6]])
    matrix_5 = matrix_4 + result_1
    print(matrix_5)
