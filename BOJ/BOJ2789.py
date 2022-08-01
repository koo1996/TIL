remove_list = ['C','A','M','B','R','I','D','G','E']

N = input()
for i in remove_list:
    if i in N:
        N = N.replace(i,'')
print(N)