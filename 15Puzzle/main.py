import node
import bfs
import dfs
import AStar

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
    test_helper1 = node.node(puzzle, board_height, board_width, 'LRUD')
    print("A*hamm" + str(AStar.AStar(test_helper1, 'hamm')))

    test_helper2 = node.node(puzzle, board_height, board_width, 'LRUD')
    print("A*manh" + str(AStar.AStar(test_helper2, 'manh')))

    test_helper3 = node.node(puzzle, board_height, board_width, 'LRUD')
    print("BFS" + str(bfs.bfs(test_helper3)))

    test_helper4 = node.node(puzzle, board_height, board_width, 'LRUD')
    print("DFS" + str(dfs.dfs(test_helper4)))
