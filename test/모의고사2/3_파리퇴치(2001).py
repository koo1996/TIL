T = int(input()) #테스트 케이스 설정

for test in range(1,T+1):
    N,M = map(int,input().split())
    # N x N matrix 생성 
    matrix = [list(map(int,input().split())) for i in range(N)]
    # 빈 리스트 생성
    result = []
    # 0부터 N-M자리 까지 반복 (파리채크기만큼 빼지않으면 범위가 넘어간다.)
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            #파리채크기만큼 해당되는 행렬의 합을 구하고 누적합을 result에 저장  
            for x in range(i,i+M):                 
                for y in range(j,j+M):
                    sum += matrix[x][y]
            result.append(sum)
    print(f'#{test}',max(result)) #결과값 출력.