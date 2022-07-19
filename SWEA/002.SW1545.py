N = int(input()) 
for test_case in range(N+2,1,-1): #N+1 반복
    N=N-1 # -1 씩 작아진다.
    print(N+1, end=' ') # 결과값 출력