T = int(input())

for test in range(1,T+1):
    N,K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        cnt = 0        #cnt 초기화
        #열을 검사하는 코드
        for j in range(N):
            if matrix[i][j] == 1: #1이 있다면 cnt 1씩 증가
                cnt += 1
            if matrix[i][j] == 0 or j == N-1: #0이거나 줄에 마지막 자리면 
                if cnt == K: #cnt가 K면 result 1씩 증가
                    result += 1
                cnt = 0 #아니면 cnt 초기화
        
        #행을 검사하는 코드
        for j in range(N): 
            if matrix[j][i] == 1: #1이 있다면 cnt 1씩 증가
                cnt += 1
            if matrix[j][i] == 0 or j == N-1: #0이거나 줄에 마지막 자리면
                if cnt == K: #cnt가 k면 result 1씩 증가
                    result += 1
                cnt = 0 #아니면 cnt 초기화
    print(f'#{test}',result) #결과값 출력