#둘 다 True 일 경우에만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a,b = input().split()

if bool(int(a)) and bool(int(b)) == True:
    print('True')
else:
    print('False')
