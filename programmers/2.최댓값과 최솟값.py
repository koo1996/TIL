def solution(s):
    s_ = list(map(int, s.split()))
    return str(min(s_)) + " " + str(max(s_))