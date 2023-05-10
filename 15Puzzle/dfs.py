import time


def dfs(node):
    order = node.order
    MaxDepth = 20
    S = []  # Stos
    T = set()  # Lista stanów zamkniętych
    S.append(node)
    it = 0
    start = time.time()
    while S:
        it += 1
        v = S.pop()
        if v.hash() not in T and v.depth < MaxDepth:
            v.depth += 1
            if v.is_solved():
                end = time.time()
                return len(v.solution), v.solution, end - start, len(T), it
            T.add(v.hash())
            for direction in order:
                v.change_state(direction)
            for neighbour in reversed(v.neighbours):
                S.append(neighbour)
