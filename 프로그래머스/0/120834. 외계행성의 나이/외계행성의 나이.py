def solution(age):
    a=''
    for i in str(age):
        a+=chr(int(i)+97)
    return a