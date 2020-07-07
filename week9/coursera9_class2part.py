from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return "\n".join("\t".join(map(str, row)) for row in self.matrix)

    def size(self):
        matrix_size = (len(self.matrix), len(self.matrix[0]))
        return matrix_size

    def __add__(self, other):
        # other = Matrix(other)
        result = []
        new_num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                sum = self.matrix[i][j] + other.matrix[i][j]
                new_num.append(sum)
            if len(new_num) == len(self.matrix):
                result.append(new_num)
                new_num = []
        return Matrix(result)

    def __mul__(self, other):
        return Matrix([[i * other for i in row] for row in self.matrix])

    __rmul__ = __mul__


exec(stdin.read())
