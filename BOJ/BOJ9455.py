for test in range(int(input())): #테스트 케이스 설정
    N,M = map(int,input().split()) #N,M 입력
    matrix = [list(map(int,input().split())) for i in range(N)] #행렬 값 입력
    cnt = 0 #cnt 초기화
    for m in range(M): 
        for n in range(N-1): # 마지막행은 크기 비교할 필요가 없다.
            for k in range(n+1,N): #1행씩 내리면서 크기 비교
                if matrix[n][m] > matrix[k][m]: #matrix[n][m]가 크면 cnt 1씩 증가
                    cnt += 1
    print(cnt)