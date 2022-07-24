for test in range(1,int(input())+1):
    number = list(map(int,input().split()))
    result = max(number)
    print('#{} {}'.format(test,result))