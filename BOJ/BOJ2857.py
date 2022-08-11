Name_ = [input() for i in range(5)]
result = []
for i in range(len(Name_)):
    if 'FBI' in Name_[i]:
        result.append(i+1)
if result == []:
    print('HE GOT AWAY!')
else:
    print(*result)