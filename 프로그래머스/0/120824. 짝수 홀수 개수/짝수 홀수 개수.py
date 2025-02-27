def solution(num_list):
    a=[0,0]
    for i in num_list:
        a[i%2]+=1
    return a