def solution(A):
    for i in A:
        if i=='l':
            return A[:A.index(i)]
        elif i=='r':
            return A[A.index(i)+1:]
    return []
    
  