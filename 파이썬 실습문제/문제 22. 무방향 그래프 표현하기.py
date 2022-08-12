import pprint

N,M = map(int,input().split()) #정점의 개수 N, 간선의 개수 M을 입력

graph = [[0] * (N+1) for _ in range(N+1)] # 7 x 7 행렬 만들기 
graph2 = [[] for _ in range(N+1)] # 비어있는 행렬 만들기
for i in range(M):
    A,B = map(int,input().split()) 
    graph[A][B] = 1 #A,B 해당하는 위치에 1대입
    graph[B][A] = 1 #B,A 해당하는 위치에 1대입
    graph2[A].append(B) #graph2[A] 에 B 대입
    graph2[B].append(A) #graph2[B] 에 A 대입
pprint.pprint(graph)
print(graph2)