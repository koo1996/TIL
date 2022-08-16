A,B = map(int,input().split())
if B - 45 < 0:
    B = 60 + (B - 45)
    if A == 0:
        print(23,B)
    else:
        print(A-1,B)
elif B - 45 >= 0:
    print(A,B-45)
