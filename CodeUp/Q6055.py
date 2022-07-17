#하나라도 참일 경우 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a,b = input().split()

if bool(int(a)) or bool(int(b)):
    print('True')
else:
    print('False')