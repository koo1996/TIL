result1 = []

for i in range(1,10000):

    if i >= 1000: #4536
        sum = i + (i // 1000) + ((i % 1000) // 100) + ((i % 100) // 10) + (i % 10)
        result1.append(sum)
    elif i >=100: #124
        sum = i + (i // 100) + ((i % 100) // 10) + (i % 10)
        result1.append(sum)
    elif i >=10:
        sum = i + (i // 10) + (i % 10)
        result1.append(sum)
    elif i >= 1:
        sum = i + i
        result1.append(sum)

for j in range(1,10000):
    if j not in result1:
        print(j)