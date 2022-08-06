Player = int(input())

matrix = [list(map(int,input().split())) for _ in range(Player)] #N x M에 입력값을 넣은 행렬을 만든다.

for i in range(Player):
    sum = 0 #sum 초기화
    for j in range(3): 
        for k in range(Player):
            if i == k: #i 와 k가 같으면 통과한다. 중복제거
                continue
            elif matrix[i][j] == matrix[k][j]: #두 값이 같으면 break한다.
                answer = 0
                break
            else:
                answer = 1 #두 값이 다르면 answer = 1 저장
        if answer == 1: #for문을 돌고 결과값이 1이면 matrix[i][j]을 sum에 저장한다
            sum += matrix[i][j] #3열까지 진행해 sum에 저장한다.
    print(sum) #sum 출력