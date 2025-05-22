def solution(p, s):
    arr2=[]
    for i in range(len(s)):
        if (100-p[i])%s[i]>0:
            arr2.append(((100-p[i])//s[i])+1)
        else:
            arr2.append((100-p[i])//s[i])
    result=[]
    current=arr2[0]
    count=1
    
    for i in range(1, len(arr2)):
        if current>=arr2[i]:
            count+=1
        else:
            result.append(count)
            current=arr2[i]
            count=1
    result.append(count)
    return result
    
    