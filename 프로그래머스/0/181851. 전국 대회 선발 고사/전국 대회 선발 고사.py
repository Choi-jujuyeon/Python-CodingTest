def solution(rank, attendance):
    a=sorted([[rank[i],attendance[i],rank.index(rank[i])] for i in range(len(rank)) if attendance[i]] ,key=lambda x:x[0])
    return 10000*a[0][2]+100*a[1][2]+a[2][2]
        
        
        
    
        