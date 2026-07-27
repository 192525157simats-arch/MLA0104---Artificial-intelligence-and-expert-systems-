GBFS(Graph, Heuristic, Start, Goal)

1. Create an open_list containing:
       (node, path, heuristic_value)

2. Insert (Start, [Start], h(Start)) into open_list

3. Create an empty visited list

4. While open_list is not empty:

       Select node with smallest heuristic value

       Remove that node from open_list

       If node == Goal:
             Print path
             Print cost
             Stop

       Add node to visited

       For each neighbour of node:

             If neighbour not in visited:

                   Add (neighbour,
                        updated_path,
                        heuristic_cost)
                   to open_list
