#음수이면서 짝수이면, A
#음수이면서 홀수이면, B
#양수이면서 짝수이면, C
#양수이면서 홀수이면, D를 출력한다.

n = int(input())

if n < 0:
    if n % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')