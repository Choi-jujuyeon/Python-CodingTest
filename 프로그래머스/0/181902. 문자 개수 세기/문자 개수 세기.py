def solution(my_string):
    a=[0]*52
    for i in my_string:
        if i.isupper():
            a[ord(i)-65]+=1
        else:
            a[ord(i)-71]+=1
    return a