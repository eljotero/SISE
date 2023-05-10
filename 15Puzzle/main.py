import helper
import bfs

if __name__ == '__main__':
    with open('1.txt', 'r') as file:
        array_size = []
        puzzle = []
        for line_number, line in enumerate(file):
            elements = line.split()
            if line_number == 0:
                array_size = elements
            else:
                for element in elements:
                    puzzle.append(int(element))
    board_height = array_size[1]
    board_width = array_size[0]
    test_helper = helper.Helper(puzzle, board_height, board_width, 'LRUD')
    print(test_helper.array)
    test_helper_2 = bfs.bfs(test_helper)
    print(test_helper_2.solution)
    print(test_helper_2.array)
