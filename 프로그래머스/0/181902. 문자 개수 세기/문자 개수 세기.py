from collections import Counter
def solution(my_string):
    c=Counter(my_string)
    a=[]
    for i in range(ord('A'),ord('Z')+1):
        a.append(c.get(chr(i),0))
    for i in range(ord('a'),ord('z')+1):
        a.append(c.get(chr(i),0))
    return a
        