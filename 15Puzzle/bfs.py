from collections import deque


def bfs(node):
    order = node.order
    Q = deque()  # Kolejka wszytkich stanów
    T = set()  # Zbiór stanów odwiedzonych
    s = node  # Węzeł
    Q.append(s)

    while Q:
        v = Q.popleft()
        if v.hash() not in T:
            T.add(v.hash())
            if v.is_solved():
                return v
            for i in range(0, len(order), 1):
                v.change_state(order[i])
            for neighbour in v.neighbours:
                Q.append(neighbour)
