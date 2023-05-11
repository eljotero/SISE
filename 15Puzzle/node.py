import copy


class node:
    def __init__(self, array, height, width, order):
        self.height = int(height)
        self.width = int(width)
        self.array = array
        self.order = order
        self.solution = ''
        self.parent = ''
        self.neighbours = []
        self.depth = 1
        self.heuristic = 0

    def is_solved(self):
        for i in range(0, len(self.array) - 1, 1):
            if self.array[i] != i + 1:
                return False
        return True

    def find_zero(self):
        for i in range(0, len(self.array), 1):
            if self.array[i] == 0:
                return i

    def make_move(self, direction):
        zero_index = self.find_zero()
        match direction:
            case "D":
                if zero_index // self.width < self.height - 1:
                    self.change_values(zero_index, zero_index + self.width)
            case "U":
                if zero_index // self.width > 0:
                    self.change_values(zero_index, zero_index - self.width)
            case "R":
                if zero_index % self.width < self.width - 1:
                    self.change_values(zero_index, zero_index + 1)
            case "L":
                if zero_index % self.width > 0:
                    self.change_values(zero_index, zero_index - 1)

    def hash(self):
        return hash(tuple(self.array))

    def change_values(self, index_of_zero, target_index):
        temp = self.array[index_of_zero]
        self.array[index_of_zero] = self.array[target_index]
        self.array[target_index] = temp

    def change_state(self, direction):
        new_node = copy.deepcopy(self)
        match direction:
            case "D":
                if self.find_zero() // self.width < self.height - 1 and self.parent != "U":
                    new_node.parent = direction
                    new_node.solution += "D"
                    new_node.make_move(direction)
                    self.neighbours.append(new_node)
            case "U":
                if self.find_zero() // self.width > 0 and self.parent != "D":
                    new_node.parent = direction
                    new_node.solution += "U"
                    new_node.make_move(direction)
                    self.neighbours.append(new_node)
            case "R":
                if self.find_zero() % self.width < self.width - 1 and self.parent != "L":
                    new_node.parent = direction
                    new_node.solution += "R"
                    new_node.make_move(direction)
                    self.neighbours.append(new_node)
            case "L":
                if self.find_zero() % self.width > 0 and self.parent != "R":
                    new_node.parent = direction
                    new_node.solution += "L"
                    new_node.make_move(direction)
                    self.neighbours.append(new_node)

    def hamming(self):
        metric_value = 0
        target_array = []
        for i in range(0, len(self.array), 1):
            target_array.append(i + 1)
        for i in range(0, len(self.array), 1):
            if target_array[i] != self.array[i] and self.array[i] != 0:
                metric_value += 1
        return metric_value

    def manhattan(self):
        two_dimensional_array = [[0 for _ in range(self.width)] for _ in range(self.height)]
        goal_array = [[0 for _ in range(self.width)] for _ in range(self.height)]
        k = 1
        metric_value = 0
        for i in range(self.height):
            for j in range(self.width):
                goal_array[i][j] = k
                two_dimensional_array[i][j] = self.array[i * self.width + j]
                k += 1
        for i in range(self.height):
            for j in range(self.width):
                if two_dimensional_array[i][j] != 0:
                    temp = two_dimensional_array[i][j]
                    goal_row = self.get_row_index(goal_array, temp)
                    goal_column = self.get_column_index(goal_array, temp)
                    metric_value += abs(i - goal_row) + abs(j - goal_column)
        return metric_value

    def get_row_index(self, array, value):
        for i, row in enumerate(array):
            if value in row:
                return i

    def get_column_index(self, array, value):
        for i, row in enumerate(array):
            if value in row:
                return row.index(value)

    def __lt__(self, other):
        return self.heuristic < other.heuristic
