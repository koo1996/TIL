#1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
#3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.


n = int(input())
for i in range(1,n+1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('X', end=' ')
    else:
        print(i, end=' ')





#n = int(input())
#count=0

#while count<n:
#    count+=1
    
#    if count % 3 == 0:
#        print('X', end=' ')
#    else:
#        print(count, end=' ')
    