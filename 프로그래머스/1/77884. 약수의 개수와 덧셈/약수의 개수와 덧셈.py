import math
def solution(left, right):
    result=0
    #약수의 개수를 알아야 한다. == 제곱근 활용
    for i in range(left,right+1):
        count=0
        for j in range(1,int(math.sqrt(i))+1):
            if i%j==0:
                if j==i//j:
                    count+=1
                else:
                    count+=2
        if count%2==0:
            result+=i
        else:
            result-=i
    return result