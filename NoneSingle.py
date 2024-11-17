from collections import deque
from collections import defaultdict


# implementation from https://celerdata.com/glossary/breadth-first-search-bfs and https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/


def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the 
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is 
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph 
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the 
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the 
                # neighbour node is the goal
                if neighbour == goal:
                    #print("Shortest path = ", *new_path)
                    print(len(new_path)-1)
                    return
            explored.append(node)
 
    # Condition when the nodes 
    # are not connected
    print(-1)
    return

# Example usage
if __name__ == "__main__":

    n, m, r = map(int, input().strip().split())
    start, end = input().split()
    V = []
    R = []

    for i in range(n):
        temp = input()
        if ("*" in temp and (temp.split(" ")[0]!= end and temp.split(" ")[0]!= start)):
            R.append(temp.split(" ")[0])
            
        else:
            V.append(temp)

    

    graph = defaultdict(list)
    
    for i in range(m):
        u, direction, v = input().split()
        if (u in R or v in R):
            continue        
        match direction:
            case "--":
                graph[u].append(v)
                graph[v].append(u)
            case "->":
                graph[u].append(v)
            #case "<-":
            #    graph[v].append(u)


    BFS_SP(graph, start, end)

