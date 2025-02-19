def solution(my_string, m, c):
    a=[]
    for i in range(0,len(my_string),m):
        a.append(list(my_string[i:i+m]))
        
    return ''.join([i[c-1] for i in a])
        