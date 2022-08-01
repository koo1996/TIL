A,B = input().split('(^0^)')

cnt1 = 0
cnt2 = 0
for i in A:
    if i == '@':
        cnt1 += 1

for j in B:
    if j == '@':
        cnt2 += 1
print(cnt1,cnt2)