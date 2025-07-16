def solution(s, n):
    res=""
    for char in s:
        if char==" ":
            res +=" "
        elif char.isupper():
            res+= chr((ord(char)-ord('A') +n)%26+ord('A'))
        elif char.islower():
            res+=chr((ord(char)-ord('a')+n)%26+ord('a'))
    return res
        