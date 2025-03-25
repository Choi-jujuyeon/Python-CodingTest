def solution(dartResult):
    result=[]
    prev=0
    arr=['S','D','T']
    dartResult=dartResult.replace('10','a')
    for i in dartResult:
        if i=='a':
            prev=10
        elif i.isdigit():
            prev=int(i)
        elif i in arr:
            result.append(prev**(arr.index(i)+1))
        elif i=='*':
            if len(result)==1:
                result[-1]=result[-1]*2
            else:
                result[-1]*=2
                result[-2]*=2
        elif i=='#':
            result[-1]*=-1
    return sum(result)
        
    