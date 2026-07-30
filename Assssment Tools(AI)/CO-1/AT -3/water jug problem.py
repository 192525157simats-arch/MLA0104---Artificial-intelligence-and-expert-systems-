from collections import deque

jug1 = 11
jug2 = 9
target = 8

visited = set()
queue = deque()

queue.append(((0,0), []))

while queue:
    (a,b), path = queue.popleft()

    if a == target or b == target:
        print("Solution Found!\n")
        for step in path:
            print(step)
        print("Final State:", (a,b))
        break

    if (a,b) in visited:
        continue

    visited.add((a,b))

    next_states = []

    next_states.append(((jug1,b),"Fill Jug1"))
    next_states.append(((a,jug2),"Fill Jug2"))
    next_states.append(((0,b),"Empty Jug1"))
    next_states.append(((a,0),"Empty Jug2"))

    transfer = min(a,jug2-b)
    next_states.append(((a-transfer,b+transfer),"Pour Jug1 -> Jug2"))

    transfer = min(b,jug1-a)
    next_states.append(((a+transfer,b-transfer),"Pour Jug2 -> Jug1"))

    for state, action in next_states:
        if state not in visited:
            queue.append((state,path+[action]))
