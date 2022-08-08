for i in range(int(input())):
    S = int(input()) #S는 가격
    for j in range(int(input())): #옵션갯수 입력
        q, p = map(int,input().split()) 
        S += q * p #옵션값을 차 가격에 누적합을 해준다.
    print(S)