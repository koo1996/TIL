import pprint

N,M = map(int,input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
for i in range(M):
    A,B = map(int,input().split())
    graph[A][B] = 1
    graph2[A].append(B)

pprint.pprint(graph)
print(graph2)