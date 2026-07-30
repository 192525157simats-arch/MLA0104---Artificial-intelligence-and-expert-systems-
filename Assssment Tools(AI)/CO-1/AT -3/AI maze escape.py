from collections import deque

maze = [
    ['S', '0', '1', '0', '0'],
    ['1', '0', '1', '0', '1'],
    ['0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '0'],
    ['0', '0', '0', 'G', '0']
]

rows = len(maze)
cols = len(maze[0])

start = None
goal = None

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

queue = deque()
queue.append((start, 0))
visited = set()
visited.add(start)

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    (x, y), steps = queue.popleft()

    if (x, y) == goal:
        print("Goal Found!")
        print("Shortest Steps =", steps)
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols:
            if maze[nx][ny] != '1' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
