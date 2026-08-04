AStar(Graph, Heuristic, Start, Goal)

1. Create an open_list containing:
       (node, cost_from_start, path)

2. Add (Start, 0, [Start]) to open_list

3. Create an empty list called closed

4. While open_list is not empty:

       Select node with lowest
       f(n) = g(n) + h(n)

       Remove that node from open_list

       If node == Goal:
             Print path
             Print total cost
             Stop

       Add node to closed

       For each neighbour of node:

             If neighbour not in closed:

                   new_cost = g + edge_cost

                   Add (neighbour, new_cost, updated_path)
                   to open_list
