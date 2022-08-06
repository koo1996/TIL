for i in range(1,int(input())+1):
    N = list(input())
    count = 1
    for j in range(len(N)):
        if N[j] == '-':
            result = result - count
        else:
            print(len(N))