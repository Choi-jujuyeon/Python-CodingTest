def solution(prices):
    a = []
    for i in range(len(prices)):
        count=0
        for j in range(i+1,len(prices)):
            count+=1
            if prices[i]>prices[j]:
                break
        a.append(count)
    return a