for i in range(1,int(input())+1): 
    N = list(map(int,input().split()))
    if N[0] == N[1] == N[2]: #3개의 숫자가 같으면 N[0] 출력
        print('#{} {}'.format(i,N[0]))
    elif N[0] == N[1]: #첫번째 숫자와 두번째 숫자 같으면 세번째 숫자 출력
        print('#{} {}'.format(i,N[2]))
    elif N[1] == N[2]: #두번째 숫자와 세번째 숫자 같으면 첫번째 숫자 출력
        print('#{} {}'.format(i,N[0]))
    elif N[0] == N[2]: #첫번째 숫자와 세번째 숫자 같으면 두번째 숫자 출력 
        print('#{} {}'.format(i,N[1]))