import node
import bfs
import dfs
import AStar
import sys

if __name__ == '__main__':
    algorithm_type = sys.argv[2]
    if algorithm_type == 'astr':
        metric = sys.argv[3]
        file = sys.argv[4]
        result_file = sys.argv[5]
        stats_file = sys.argv[6]
    else:
        order = sys.argv[3]
        file = sys.argv[4]
        result_file = sys.argv[5]
        stats_file = sys.argv[6]
    with open(f"puzzles/{file}", 'r') as file:
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
    if algorithm_type == 'bfs':
        test_helper1 = node.node(puzzle, board_height, board_width, order)
        bfs.bfs(test_helper1, result_file, stats_file)
    if algorithm_type == 'dfs':
        test_helper2 = node.node(puzzle, board_height, board_width, order)
        dfs.dfs(test_helper2, result_file, stats_file)
    if algorithm_type == 'astr':
        test_helper3 = node.node(puzzle, board_height, board_width, 'LRUD')
        AStar.AStar(test_helper3, metric, result_file, stats_file)
