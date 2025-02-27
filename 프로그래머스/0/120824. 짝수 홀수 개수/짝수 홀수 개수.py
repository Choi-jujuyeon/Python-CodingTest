def solution(num_list):
    a=len([i for i in num_list if i%2==0 ])
    return [a,len(num_list)-a]