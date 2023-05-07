import numpy as np


class Helper:
    def __init__(self, array, height, width, order):
        self.height = int(height)
        self.width = int(width)
        self.array = array
        self.order = order
        self.solution = ''

    def is_solved(self):
        array_helper = np.array(self.array)
        result = array_helper.flatten().astype(int)
        for i in range(0, result.size - 1, 1):
            if result[i] != i + 1:
                return False
        return True

    def find_zero(self):
        for i in range(0, self.width, 1):
            for j in range(0, self.height, 1):
                if self.array[i][j] == 0:
                    return i, j

    def make_move(self, direction):
        array_index_x = self.find_zero()[0]
        array_index_y = self.find_zero()[1]
        match direction:
            case "D":
                if array_index_x + 1 <= self.height:
                    self.array[array_index_x][array_index_y], self.array[array_index_x + 1][array_index_y] = \
                        self.array[array_index_x + 1][
                            array_index_y], self.array[array_index_x][array_index_y]
            case "U":
                if array_index_x - 1 >= 0:
                    self.array[array_index_x][array_index_y], self.array[array_index_x - 1][array_index_y] = \
                        self.array[array_index_x - 1][
                            array_index_y], self.array[array_index_x][array_index_y]
            case "R":
                if array_index_y + 1 <= self.width:
                    self.array[array_index_x][array_index_y], self.array[array_index_x][array_index_y + 1] = \
                        self.array[array_index_x][
                            array_index_y + 1], self.array[array_index_x][array_index_y]
            case "L":
                if array_index_y - 1 >= 0:
                    self.array[array_index_x][array_index_y], self.array[array_index_x][array_index_y - 1] = \
                        self.array[array_index_x][
                            array_index_y - 1], self.array[array_index_x][array_index_y]

    def deep_copy_of_object(self):
        object_copy = self.deep_copy_of_object()
        return object_copy
