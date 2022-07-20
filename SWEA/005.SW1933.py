N = int(input()) 

for test in range(1,N+1): #N번 반복
    if N % test == 0: #10의 약수는 나머지가 0인 값들이다.
        print(test, end=' ') 