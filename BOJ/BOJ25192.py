result = []
gom = 0
for i in range(int(input())):
    log_list = input()
    result.append(log_list)


set_ = set()
for log in result:
    if log == "ENTER":
        set_.clear()
    
    else:
        if log not in set_:
            set_.add(log)
            gom += 1
    
print(gom)