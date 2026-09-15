# Minimum Spanning Tree using Kruskal's Algorithm

# Function to find the parent
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


# Function to join two sets
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


# Kruskal's algorithm
def kruskal(graph, vertices):
    graph.sort(key=lambda x: x[2])

    parent = []
    rank = []

    for i in range(vertices):
        parent.append(i)
        rank.append(0)

    mst = []
    cost = 0

    for u, v, weight in graph:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst.append((u, v, weight))
            cost += weight
            union(parent, rank, x, y)

    print("Minimum Spanning Tree:")

    for u, v, weight in mst:
        print(u, "-", v, "=", weight)

    print("Minimum Cost =", cost)


# Graph
graph = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

# Number of vertices
vertices = 4

# Call function
kruskal(graph, vertices)