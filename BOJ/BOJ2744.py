N = input()
M = ""
for i in N:
    if i.islower():
        M += i.upper()
    else:
        M += i.lower()
print(M)