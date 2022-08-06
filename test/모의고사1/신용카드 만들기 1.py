for i in range(1,int(input())+1): 
    N = list(map(int,input().split()))
    sum1 = 0
    sum2 = 0
    for j in range(0,len(N),2): # N리스트에서 0부터 2씩 커지는 값들에 2를 곱하고 더한다.
        sum1 = sum1 + N[j] * 2
    for k in range(1,len(N),2): # N리스트에서 1부터 2씩 커지는 값들을 더한다.
        sum2 = sum2 + N[k]
    if ((sum1 + sum2) % 10) != 0: #sum1 와 sum2를 더하고 10으로 나눈 나머지를 구한다.
        result = 10 - ((sum1 + sum2) % 10) #나머지가 0이 아니면 10 - result 출력
        print('#{} {}'.format(i,result))
    else: # 나머지가 0이면 출력
        print('#{} {}'.format(i,'0'))