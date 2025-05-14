a=int(input())
count=0
next=a
while True:
    if next<10:    #일의 자리일 경우
        a1=next
        a2=0
    else:
        a1=next%10
        a2=next//10
    next=(a1+a2)%10+(next%10)*10
    count+=1
    if a==next:
        break
print(count)