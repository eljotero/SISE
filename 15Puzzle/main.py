import helper

if __name__ == '__main__':
    with open('1.txt', 'r') as file:
        array_size = []
        puzzle = []
        for line_number, line in enumerate(file):
            elements = line.split()
            if line_number == 0:
                array_size = elements
            else:
                puzzle.append(elements)
    board_height = array_size[1]
    board_width = array_size[0]
    test_helper = helper.Helper(puzzle, board_height, board_width, 'LRUD')
