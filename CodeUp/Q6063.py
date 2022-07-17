#두 정수 중 큰 값을 10진수로 출력한다.

a,b = input().split()
if int(a) < int(b):
    print(b)
else:
    print(a)