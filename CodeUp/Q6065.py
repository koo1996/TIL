#짝수만 순서대로 줄을 바꿔 출력한다.

a,b,c = input().split()
n=a,b,c
for i in n:
    if int(i) % 2 == 0:
        print(i)
