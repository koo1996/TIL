T = int(input())

for test in range(1,T+1): # 테스트 케이스 설정
    result = [] # 빈 리스트 생성
    N, K = map(int,input().split()) 
    submit = list(map(int,input().split()))
    for i in range(1,N+1): # 1부터 N번까지 반복
        if i not in submit: # submit 안에 i가 없으면 i를 result에 저장
            result.append(i)
    print(f'#{test}', *result) # 결과값 출력