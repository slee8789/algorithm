graph = [
    [],  # 숫자가 8까지있을 때, 9개 아이템 0인덱스 비우기. 0 인덱스는 무시 메모리적으로 더 효율.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9       # 방문된 정보 배열 초기화

# 재귀 사용
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 반복문 사용
def bfs(graph, start, visited):
    from collections import deque

    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# dfs(graph, 1, visited)
bfs(graph, 1, visited)