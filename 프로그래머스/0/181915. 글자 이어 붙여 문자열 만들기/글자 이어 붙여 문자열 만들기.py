def solution(my_string, index_list):
    a=[]
    for i in index_list:
            a.append(my_string[i])
    return ''.join(a)