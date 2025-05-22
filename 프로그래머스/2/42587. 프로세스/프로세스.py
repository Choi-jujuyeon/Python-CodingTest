from collections import deque
def solution(priorities, location):
    q=deque((idx,num) for idx,num in enumerate(priorities))  
    count=0 #몇개를 내보낼수있는지
    
    while q:
        current=q.popleft()
        if any(current[1] < i[1] for i in q):
            q.append(current)
            
        else:
            count+=1
            #인덱스 값이 찾는 값이랑 같을 경우
            if current[0] == location:
                return count
            
            
            
    
            
        
    
    