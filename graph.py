from collections import defaultdict
from collections import deque

def findPath(graphs, start, end):
    g = defaultdict(list)
    for node, nei in graphs:
        g[node].append(nei)
 
    visited = [False]*len(g)
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for i in g[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    return False

def bfsVisit(graphs, start):
    ret = []

    g = defaultdict(list)
    for node, nei in graphs:
        g[node].append(nei)

    visited = [False]*len(g)
    queue = deque()
    queue.append(start)
    visited[start] = True
    ret.append(start)

    while queue:
        node = queue.popleft()
        for i in g[node]:
            if not visited[i]:
                ret.append(i)
                queue.append(i)
                visited[i] = True
    return ret

def dfsVisit(graphs, start):
    g = defaultdict(list)
    for node, nei in graphs:
        g[node].append(nei)

    visited = [False]*len(g)
    helper(g, start, visited)
    
def helper(g, start, visited):
    visited[start] = True
    print start

    for i in g[start]:
        if visited[i] == False:
            helper(g, i, visited)

def genEdges(graphs):
    edges = []
    for node in g:
        for neighbor in g[node]:
            edges.append([node, neighbor])
    return edges

def buildGraph(graphs):
    graph = defaultdict(list)
    for node, neighbor in graphs:
        graph[node].append(neighbor)
    return graph

def buildGraph2(graphs, n):
    graph = {i: set() for i in range(1,n+1)}
    for node, neighbor in graphs:
        graph[node].add(neighbor)

    return graph

def buildInDrgree(graphs):
    g = defaultdict(list)
    for node, nei in graphs:
        g[node].append(nei)

    inDegree = [0 for i in range(len(g))]
    for node, nei in graphs:
        inDegree[node] += 1

    return inDegree


g = { "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
    }

g2 = [['a', 'd'], ['c', 'b'], ['c', 'c'], ['c', 'd'], ['c', 'e'], ['b', 'c'], ['e', 'c'], ['d', 'a'], ['d', 'c']]

g1 = [[0,1], [0,2], [1,2], [2,0], [2,3], [3,3]]
#print genEdges(g)
#print buildGraph(g2)
#print buildGraph2(g1, 5)
#print findPath(g1, 1, 3)
#print bfsVisit(g1, 2)
#dfsVisit(g1, 2)
print buildInDrgree(g1)


