n = int(input())

nums_ = 1  
cnt = 1
while n > nums_ :
    nums_ += 6 * cnt  
    cnt += 1  
print(cnt)