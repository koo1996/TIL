N = int(input())
Size_ = list(map(int,input().split()))
cnt = 0
max_sum = 0
for test_1 in range(1,len(Size_)):
    if Size_[test_1] > Size_[test_1 - 1]: 
        cnt = cnt + Size_[test_1] - Size_[test_1 - 1]
        max_sum = max(max_sum, cnt) 

    else:
        cnt = 0     
print(max_sum)
