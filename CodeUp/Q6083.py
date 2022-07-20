#만들 수 있는 rgb 색의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로
#줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력한다.

a,b,c = map(int,input().split())
cnt=0
for x in range(0,a):
    for y in range(0,b):
        for z in range(0,c):
            cnt+=1
            print('%d %d %d' %(x,y,z))
print(cnt)