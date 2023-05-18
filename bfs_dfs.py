def createEdge(n1, n2, adj, isVisited):
    isVisited[n1] = False
    isVisited[n2] = False

    if n1 in adj:
        adj[n1].append(n2)
    else:
        adj[n1] = [n2]
    if n2 in adj:
        adj[n2].append(n1)
    else:
        adj[n2] = [n1]

def dfs(n, adj, isVisited):
    print(n, end=" ")
    isVisited[n] = True
    for i in adj[n]:
        if isVisited[i] == False:
            dfs(i, adj, isVisited)

def bfs(node, adj, isVisited):
    queue = []
    queue.append(node)
    isVisited[node] = True

    while len(queue) > 0:
        node = queue[0]
        print(node, end=" ")
        queue.pop(0)

        for i in adj[node]:
            if isVisited[i] == False:
                queue.append(i)
                isVisited[i] = True

# main function
nodes = int(input("Enter the number of nodes: "))
edges = int(input("Enter the number of edges: "))

adj = {}
isVisited = {}

for i in range(edges):
    a, b = input(f"Enter the nodes forming edge {i+1}: ").split()
    createEdge(a, b, adj, isVisited)
print()

start = input("Enter the starting node for DFS: ")
print("The order of DFS traversal is: ", end="")
dfs(start, adj, isVisited)

for node in isVisited:
    isVisited[node] = False
print()
print()

start = input("Enter the starting node for BFS: ")
print("The order of BFS traversal is: ", end="")
bfs(start, adj, isVisited)
