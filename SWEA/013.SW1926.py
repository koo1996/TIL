# for test in range(1,int(input())+1): #input번 반복
#     result=[]
#     if test % 3 != 0: #나누기3 했을때 나머지 0이면
#         result.append(test)
#     else:
#         result.append('-')
#     print(*result, end=' ')

N = int(input())
number = list(map(str,range(1,N+1)))
cnt=0
for test in number:
    if number == '3': 
        cnt+=1
    print(cnt)

#     cnt+=1
#     number.replace(number,'-'*cnt)
# print(number)
