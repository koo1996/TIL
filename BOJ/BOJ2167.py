N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)] #N x M에 입력값을 넣은 행렬을 만든다.

K = int(input())
for _ in range(K):
    sum = 0
    i,j,x,y = map(int,input().split()) #i,j,x,y의 변수값을 선언한다.
    for test_1 in range(i-1,x): #N,M의 범위를 맞추기 위해 i,j에 -1씩 한다.
        for test_2 in range(j-1,y):
            sum += matrix[test_1][test_2] #해당되는 범위에 있는 입력값들을 더해준다.  
    print(sum)