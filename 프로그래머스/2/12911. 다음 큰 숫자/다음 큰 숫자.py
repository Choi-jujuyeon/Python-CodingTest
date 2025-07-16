def solution(n): 
    result=n
    while True:
        if result>n:
            if bin(n).count('1') == bin(result).count('1'):
                return result
        result+=1