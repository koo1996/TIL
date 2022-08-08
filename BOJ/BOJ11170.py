for test in range(int(input())): #테스트 케이스 설정
    cnt = 0 #cnt 초기화
    N, M = map(int,input().split())    
    for i in range(N,M+1): #N ~ M까지 반복
        C = str(i) #정수형 i를 문자형 i로 바꾼다.
        cnt += C.count('0') #'0'의 갯수를 세고 cnt에 저장
    print(cnt) #결과값 출력