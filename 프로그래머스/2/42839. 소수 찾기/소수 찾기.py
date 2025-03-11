from itertools import permutations

def solution(numbers):
    result_set=set()
    
    #01. 모든 조합 만들기
    for i in range(len(numbers)):
        #print(list(permutations(numbers,i+1)))      #permutations():문자열,리스트->iterable 가능
        com=list(map(int,map("".join,list(permutations(numbers,i+1)))))
        result_set|=set(com)
        
    #02. 에라토스테네스의 체 사용
    result_set-=set(range(0,2))
    end=int(max(result_set)**0.5)+1
    
    for i in range(2,end):      #배수 값 빼주기
        result_set-=set(range(i*2,max(result_set)+1,i))
    
    return len(result_set)
    
    
        
