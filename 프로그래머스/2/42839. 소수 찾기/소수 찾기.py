from itertools import permutations
def solution(numbers):
    
    #step01. 모든 숫자의 조합을 만든다.
    prime_set=set()
    for i in range(len(numbers)):
        numbers_permutation=permutations(list(numbers), i+1)       
        numbers_per_list=list(map(int,map("".join,numbers_permutation)))        
        prime_set |=set(numbers_per_list)
    
    #step 02.0과 1을 집합으로 만들고 빼쥐
    prime_set-=set(range(0,2))
    
    #step03. 에라토스테네스의 체 활용
    lim=int(max(prime_set)**0.5)+1       #핵심코드
    for i in range(2,lim):
        prime_set -= set(range(i*2,max(prime_set)+1,i))
    return len(prime_set)  