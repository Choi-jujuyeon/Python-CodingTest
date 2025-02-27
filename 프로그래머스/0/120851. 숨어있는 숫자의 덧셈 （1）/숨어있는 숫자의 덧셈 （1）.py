def solution(my_string):
    
    return sum([int(i) for i in my_string.upper() if not ('A'<=i<='Z')])