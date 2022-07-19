T = int(input())
res=[]
for test_case in range(1,T+1):
    a,b = input().split()
    if int(a) < int(b):
        res.append('#%d <' %test_case)
    elif int(a) > int(b):
        res.append('#%d >' %test_case)
    else:
        res.append('#%d =' %test_case)

print(*res, sep='\n')
