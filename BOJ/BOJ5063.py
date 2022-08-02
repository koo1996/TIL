N = int(input())

for i in range(N):
    A,B,C = map(int,input().split())
    if A < B-C: 
        print('advertise')
    elif A > B-C:
        print('do not advertise')
    else:
        print('does not matter')