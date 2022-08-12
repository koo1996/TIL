grade_ = list(map(int,input().split()))

if sum(grade_) >= 100:
    print('OK')
else:
    if grade_.index(min(grade_)) == 0:
        print('Soongsil')
    elif  grade_.index(min(grade_)) == 1:
        print('Korea')
    else:
        print('Hanyang')
