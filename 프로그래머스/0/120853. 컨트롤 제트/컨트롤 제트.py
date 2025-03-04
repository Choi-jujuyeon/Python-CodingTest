def solution(s):
    s=s.split()
    for i in range(len(s)):
        if s[i]=='Z':
            s[i-1],s[i]=0,0
        else:
            s[i]=int(s[i])
    return sum(s)
    