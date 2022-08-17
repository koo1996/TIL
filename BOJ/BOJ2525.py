A,B = map(int,input().split())
N = int(input())

if B + N >= 60:        
    min_ = (B + N) % 60
    hour_ = A + (B + N) // 60 
    if hour_ >= 24:
        hour_o = hour_ -24
        print(hour_o,min_)
    else:
        print(int(hour_) , min_)
else:
    print(A,B + N)