T = int(input())

for test in range(1,T+1): #테스트케이스 설정
    n, m = map(int, input().split()) #입력값
    graph = [[] for _ in range(n+1)] #빈 리스트 생성
    visited = [False] * (n+1) #방문 유무

    for _ in range(m): #무방향 리스트 생성
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    def dfs(v): #DFS / visited[v] True로 바꾸고 리스트에 있는 정수를 차례대로 입력한다.
        visited[v] = True
        for i in graph[v]: #visited 리스크에 False 면 True로 바꾸고 i를 넣고 함수를 다시 돌린다.
            if visited[i] == False:
                visited[i] = True
                dfs(i)

    count = 0
    for i in range(1, n+1): #visited 리스트 False가 있으면 count +1 해준다.
        if visited[i] == False:
            count+=1
            dfs(i)
    print(f'#{test}',count)