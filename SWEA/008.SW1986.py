N = int(input())

res=[]
for test in range(1,N+1):
    number = int(input())
    result=0
    for test_2 in range(1,number+1):
        if test_2 % 2 == 0:
            result = result - test_2
        else:
            result = result + test_2
        
    res.append('#%d %d' %(test,result))
    
print(*res, sep='\n') 