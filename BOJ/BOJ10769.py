N = input()

N = N.replace(':-)','1')
N = N.replace(':-(','0')

cnt1 = 0
cnt2 = 0
for i in N:
    if i == '1':
        cnt1 += 1
    elif i == '0':
        cnt2 += 1

if cnt1 > cnt2:
    print('happy')
elif cnt1 < cnt2:
    print('sad')
elif cnt1 == cnt2 == 0:
    print('none')
elif cnt1 == cnt2:
    print('unsure')