def solution(s):
    new=[]
    for i in s.split(" "):
        res=""
        for j in range(len(i)):
            if j%2!=0: #홀수
                res+=i[j].lower()
            else:
                res+=i[j].upper()
        new.append(res)
    return " ".join(new)
            