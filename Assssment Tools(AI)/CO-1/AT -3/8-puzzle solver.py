import heapq

goal = (1,2,3,4,5,6,7,8,0)

start = (1,2,3,
         4,0,6,
         7,5,8)

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def heuristic(state):
    h = 0
    for i in range(9):
        if state[i] != 0:
            x1,y1 = divmod(i,3)
            x2,y2 = divmod(goal.index(state[i]),3)
            h += abs(x1-x2)+abs(y1-y2)
    return h

pq = []
heapq.heappush(pq,(heuristic(start),0,start,[]))

visited = set()

while pq:
    f,g,state,path = heapq.heappop(pq)

    if state == goal:
        print("Solved!")
        print("Moves =", len(path))
        print(path)
        break

    if state in visited:
        continue

    visited.add(state)

    zero = state.index(0)
    x,y = divmod(zero,3)

    for dx,dy in moves:
        nx,ny = x+dx,y+dy

        if 0<=nx<3 and 0<=ny<3:
            new = list(state)
            newpos = nx*3+ny
            new[zero],new[newpos] = new[newpos],new[zero]
            new = tuple(new)

            if new not in visited:
                heapq.heappush(
                    pq,
                    (g+1+heuristic(new),
                     g+1,
                     new,
                     path+[new])
                )
