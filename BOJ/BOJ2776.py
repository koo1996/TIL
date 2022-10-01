T = int(input())

for i in range(T):
    N = int(input())
    Note_1 = set(map(int,input().split()))
    M = int(input())
    Note_2 = list(map(int,input().split()))
    for j in Note_2:
        if j in Note_1:
            print('1')
        else:
            print('0')
