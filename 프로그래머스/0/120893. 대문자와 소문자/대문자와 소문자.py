def solution(my_string):
    return ''.join([i.lower() if ('A'<=i<='Z') else i.upper() for i in my_string])