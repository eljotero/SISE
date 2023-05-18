from collections import deque
import time


def bfs(node, file_name_1, file_name_2):
    order = node.order
    Q = deque()  # Kolejka wszytkich stanów
    T = set()  # Zbiór stanów odwiedzonych
    s = node  # Węzeł
    start = time.time()
    i = 0  # Liczba stanów przetworzonych
    Q.append(s)

    while Q:
        v = Q.popleft()
        if v.__hash__() not in T:
            i = i + 1
            T.add(v.__hash__())
            if v.is_solved():
                end = time.time()
                with open(f"results/{file_name_1}", "w") as output_file:
                    output_file.write("Rozwiazanie: " f"{v.solution}\n")
                with open(f"results/{file_name_2}", "w") as output_file:
                    output_file.write("Dlugosc rozwizania: "f"{len(v.solution)}\n")
                    output_file.write("Czas rozwiazania: "f"{end - start}\n")
                    output_file.write("Liczba stanow otwartych: "f"{len(T)}\n")
                    output_file.write("Liczba stanow odwiedzonych: "f"{i}\n")
                return
            for direction in order:
                v.change_state(direction)
            for neighbour in v.neighbours:
                Q.append(neighbour)
