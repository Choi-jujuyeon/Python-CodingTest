def solution(a, num1, num2):
    return a[:num1]+a[num2]+a[num1+1:num2]+a[num1]+a[num2+1:]