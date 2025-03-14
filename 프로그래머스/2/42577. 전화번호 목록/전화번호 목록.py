def solution(phone_book):
    pp=sorted(phone_book)
    
    for i in range(len(pp)-1):
        if pp[i+1].startswith(pp[i]):
            return False
    return True
        