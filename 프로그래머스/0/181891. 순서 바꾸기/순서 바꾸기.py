def solution(num_list, n):
    a=num_list[n:]
    a.extend(num_list[0:n])
    return a