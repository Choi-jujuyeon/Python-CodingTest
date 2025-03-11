def solution(phone_book):
    s=sorted(phone_book)
    for a,b in zip(s,s[1:]):
        if b.startswith(a):
            return False
    return True
            
        