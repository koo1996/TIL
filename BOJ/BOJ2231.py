N = int(input())
result = 0
for i in range(1, N+1): #N번 반복
    a = list(map(int,str(i))) #i값 한자리씩 리스트에 저장한다.
    result = i + sum(a) #i + 각자리의 합
    if result == N: #result 이 입력값이면 i 출력
        print(i)
        break
    if i == N: #N번까지 반복해도 답이 없으면 0 출력
        print(0)