def solution(s):
    result=""
    first =True
    
    for char in s:
        if first:
            result+=char.upper()
        else:
            result+=char.lower()
        first=(char==" ")
    return result