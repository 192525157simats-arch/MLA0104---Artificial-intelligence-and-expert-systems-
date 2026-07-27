UCS(Graph, Start, Goal)

1. Create a list called queue storing (node, cost)

2. Insert (Start, 0) into queue

3. Create an empty visited list

4. While queue is not empty:

      Find node with minimum cost
      Remove it from queue

      If node already visited:
            Continue

      Add node to visited

      If node equals Goal:
            Print cost
            Stop

      For each neighbour of node:

            Add (neighbour, cost + weight) to queue
