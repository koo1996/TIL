stack = []

while True:
    N = input()
    if N == '.':
        break
    for i in N:
        if N == '(' or N == '[':
                stack.append()
        elif N == ')':
            if stack[-1] == '(':
                stack.pop()
             