# N * M 크기의 직사각형 형태의 미로에 갇혀있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야한다.
# 동빈이는 (1,1)이며 미로의 출구는 (N,M)이다 한번에 한칸씩 이동가능
# 이때 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어있다.
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 기수를 구하세요. 시작 칸, 마지막 칸 모두 포함한다.
# 입력 :
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 10

n, m = 5, 6
graph = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    from collections import deque
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
