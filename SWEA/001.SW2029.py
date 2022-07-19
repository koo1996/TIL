

T = int(input())
result=[]
for test_case in range(1,T+1):
    a,b = input().split()
    a=int(a)
    b=int(b)
    c = a // b 
    d = a % b
    result.append('#%d %d %d' %(test_case,c,d))

print(*result, sep='\n')