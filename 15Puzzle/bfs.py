from collections import deque
import time


def bfs(node):
    order = node.order
    Q = deque()  # Kolejka wszytkich stanów
    T = set()  # Zbiór stanów odwiedzonych
    s = node  # Węzeł
    start = time.time()
    i = 0
    Q.append(s)

    while Q:
        i = i + 1
        v = Q.popleft()
        if v.hash() not in T:
            T.add(v.hash())
            if v.is_solved():
                end = time.time()
                return len(v.solution), v.solution, end - start, len(T), i
            for direction in order:
                v.change_state(direction)
            for neighbour in v.neighbours:
                Q.append(neighbour)
