#두 값의 True / False 값이 모두 False 일 때만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

a,b = input().split()

if bool(int(a)) or bool(int(b)) == True:
    print('False')
else:
    print('True')