def solution(myStr):
    a=myStr.replace('a', ' ').replace('b',' ').replace('c', ' ').split()
    return a if a else ["EMPTY"]