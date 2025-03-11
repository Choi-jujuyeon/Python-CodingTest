def solution(phone_book):
    s=sorted(phone_book)
    for i in range(len(phone_book)-1):
        if s[i+1].startswith(s[i]):
            return False
    return True
        