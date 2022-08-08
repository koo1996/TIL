N, M = map(int,input().split()) 
Number_ = list(map(int,input().split()))
result = [] # 빈 리스트 생성
for i in range(N): #3장의 합, 모든 경우의 수를 구한다.
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = Number_[i] + Number_[j] + Number_[k]
            if sum <= M: #M보다 작거나 같으면 result에 저장
                result.append(sum)
print(max(result)) #최대값 출력