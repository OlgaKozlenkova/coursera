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


exec(stdin.read())
