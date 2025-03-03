def solution(array, n):
    return min(array, key=lambda i:(abs(n-i),i))