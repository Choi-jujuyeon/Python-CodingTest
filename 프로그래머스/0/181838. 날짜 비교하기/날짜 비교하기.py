def solution(date1, date2):
    a=''
    b=''
    for i in range(3):
        a+=str(date1[i])
        b+=str(date2[i])
    return 1 if int(a)<int(b) else 0