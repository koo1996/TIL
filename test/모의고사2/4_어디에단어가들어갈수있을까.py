T = int(input())

for test in range(1,T+1):
    N,K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        cnt = 0        
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            if matrix[i][j] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt = 0

        for j in range(N):
            if matrix[j][i] == 1:
                cnt += 1
            if matrix[j][i] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt = 0
    print(f'#{test}',result)