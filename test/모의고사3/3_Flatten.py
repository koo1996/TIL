for test in range(1,11): #테스트케이스 설정
    N = int(input()) #변경횟수
    M = list(map(int,input().split())) #입력값 리스트에 저장
    for _ in range(N): #변경횟수만큼 반복       
        High_ = max(M) #최대값 변수에 저장
        Low_ = min(M) #최소값 변수에 저장
        index_H = M.index(max(M)) #최대값 위치 변수에 저장
        index_L = M.index(min(M)) #최소값 위치 변수에 저장
        High_ -= 1 #최대값은 -1씩 해준다.
        Low_ += 1 #최소값은 +1씩 해준다.
        M[index_H] = High_ #최대값 위치에 변경된 최대값 저장
        M[index_L] = Low_ #최소값 위치에 변경된 최소값 저장
    print(f'#{test}',max(M) - min(M)) #반복문을 마친 M리스트에서 최대값 - 최소값 결과값 출력