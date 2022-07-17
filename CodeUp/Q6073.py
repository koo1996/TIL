#1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다.

n = int(input())
count = 1

while count <= n:
    n-=1
    print(n)
