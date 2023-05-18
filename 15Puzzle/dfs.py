import time


def dfs(node, file_name_1, file_name_2):
    order = node.order
    MaxDepth = 20
    S = []  # Stos
    T = set()  # Lista stanów zamkniętych
    S.append(node)
    it = 0
    start = time.time()
    while S:
        v = S.pop()
        if v.__hash__() not in T and v.depth < MaxDepth:
            it += 1
            v.depth += 1
            if v.is_solved():
                end = time.time()
                with open(f"results/{file_name_1}", "w") as output_file:
                    output_file.write("Rozwiazanie: " f"{v.solution}\n")
                with open(f"results/{file_name_2}", "w") as output_file:
                    output_file.write("Dlugosc rozwizania: "f"{len(v.solution)}\n")
                    output_file.write("Czas rozwiazania: "f"{end - start}\n")
                    output_file.write("Liczba stanow otwartych: "f"{len(T)}\n")
                    output_file.write("Liczba stanow odwiedzonych: "f"{it}\n")
                return
            T.add(v.__hash__())
            for direction in order:
                v.change_state(direction)
            for neighbour in reversed(v.neighbours):
                S.append(neighbour)
