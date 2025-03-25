def solution(dartResult):
    result=[]
    prev=0
    dartResult=dartResult.replace('10','a')
    for i in dartResult:
        if i=='a':
            prev=10
        if i.isdigit():
            prev=int(i)
        elif i=='S':
            result.append(prev)
        elif i=='D':
            result.append(prev**2)
        elif i=='T':
            result.append(prev**3)
        elif i=='*':
            if len(result)==1:
                result[-1]=result[-1]*2
            else:
                result[-1]*=2
                result[-2]*=2
        elif i=='#':
            result[-1]*=-1
    return sum(result)
        
    