import re
def solution(my_string):
    a=re.split(r'[A-Z]', my_string.upper())
    return sum([int(i) if i else 0 for i in a])
        
