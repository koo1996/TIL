#입력된 순서대로 짝(even)/홀(odd)을 줄을 바꿔 출력한다.

a,b,c = input().split()

for i in a,b,c:
    if int(i) % 2 == 0:
        print('even')
    else:
        print('odd')
