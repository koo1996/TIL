for i in range(int(input())):
    A,B = input().split()
    M = list(B)
    M[int(A)-1] = '@' 
    M.remove('@')
    print(*M,sep='')
    