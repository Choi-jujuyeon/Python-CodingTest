def solution(myString, pat):
    
    return 1 if pat.replace('A','b').replace('B','a') in myString.replace('A','a').replace('B','b') else 0
    