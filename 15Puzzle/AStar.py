from queue import PriorityQueue
import time


def AStar(node, metric):
    order = node.order
    p = PriorityQueue()
    T = set()
    i = 0
    start = time.time()
    p.put(node, 0)
    while p:
        i += 1
        v = p.get()
        if v.hash() not in T:
            if v.is_solved():
                end = time.time()
                return len(v.solution), v.solution, end - start, len(T), i
            T.add(v)
            for direction in order:
                v.change_state(direction)
            for neighbour in v.neighbours:
                if neighbour not in T:
                    if metric == 'hamm':
                        neighbour.heuristic = node.hamming()
                    if metric == 'manh':
                        neighbour.heuristic = node.manhattan()
                    g = neighbour.depth + neighbour.heuristic
                    p.put(neighbour, g)
