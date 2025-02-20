def solution(num_list):
    count=0
    for i in range(len(num_list)):
        while num_list[i]!=1:
            if num_list[i]%2==0:
                num_list[i]/=2
                count+=1
            else:
                num_list[i]=(num_list[i]-1)/2
                count+=1
    return count