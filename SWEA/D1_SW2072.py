for test in range(1,int(input())+1):
    number = list(map(int,input().split()))
    result = 0
    for test_2 in range(10):
        if number[test_2] % 2 == 1:
            result = result + number[test_2]
    print('#{} {}'.format(test,result))
    