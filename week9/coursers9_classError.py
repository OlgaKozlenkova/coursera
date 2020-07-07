from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return "\n".join("\t".join(map(str, row)) for row in self.matrix)

    def size(self):
        matrix_size = (len(self.matrix), len(self.matrix[0]))
        return matrix_size

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            lenght = len(self.matrix[0])
            for row in self.matrix:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.matrix:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            new_num = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    sum = self.matrix[i][j] + other.matrix[i][j]
                    new_num.append(sum)
                if len(new_num) == len(self.matrix[0]):
                    result.append(new_num)
                    new_num = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[i * other for i in row] for row in self.matrix])

    __rmul__ = __mul__

    def transpose(self):
        transposeMatrix = [list(i) for i in zip(*self.matrix)]
        self.matrix = transposeMatrix
        return Matrix(transposeMatrix)

    @staticmethod
    def transposed(self):
        return Matrix([list(i) for i in zip(*self.matrix)])


exec(stdin.read())
