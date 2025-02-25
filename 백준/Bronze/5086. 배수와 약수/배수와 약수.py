arr=[]
while True:
    a,b=map(int,input().split())
    if a == 0 and b == 0:
        break
    
    if b%a==0:
        arr.append("factor\n")
    elif a%b==0:
        arr.append('multiple\n')
    else:
        arr.append('neither\n')    
    if a==0 and b==0:
        break
print(''.join(arr))