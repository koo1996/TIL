A,B = map(int,input().split())

if A < B:
    if A == 1 and B == 3:
        print('A')
    else:
        print('B')
elif A > B:
    if A == 3 and B == 1:
        print('B')
    else:
        print('A')