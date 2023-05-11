from queue import PriorityQueue
import time


def AStar(node, metric, file_name_1, file_name_2):
    order = node.order
    p = PriorityQueue()
    T = set()
    i = 0
    start = time.time()
    p.put(node, 0)
    while p:
        v = p.get()
        if v.hash() not in T:
            i += 1
            if v.is_solved():
                end = time.time()
                with open(f"{file_name_1}", "w") as output_file:
                    output_file.write("Rozwiazanie: " f"{v.solution}\n")
                with open(f"{file_name_2}", "w") as output_file:
                    output_file.write("Dlugosc rozwizania: "f"{len(v.solution)}\n")
                    output_file.write("Czas rozwiazania: "f"{end - start}\n")
                    output_file.write("Liczba stanow otwartych: "f"{len(T)}\n")
                    output_file.write("Liczba stanow odwiedzonych: "f"{i}\n")
                return
            T.add(v)
            for direction in order:
                v.change_state(direction)
            for neighbour in v.neighbours:
                if neighbour not in T:
                    if metric == 'hamm':
                        neighbour.heuristic = node.hamming()
                    if metric == 'manh':
                        neighbour.heuristic = node.manhattan()
                    priority = neighbour.depth + neighbour.heuristic
                    p.put(neighbour, priority)
