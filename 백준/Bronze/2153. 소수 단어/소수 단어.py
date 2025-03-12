a=[]
for i in input():
    if 'a'<=i<='z':
        a.append(ord(i)-ord('a')+1)
    elif 'A'<=i<='Z':
        a.append(ord(i)-ord('A')+27)
if sum(a)==1:
    print("It is a prime word.")
else:
    val=True
    for i in range(2,int(sum(a)**0.5)+1):
        if sum(a)%i==0:
            val=False
            break
    if val:
        print("It is a prime word.")
    else:
        print("It is not a prime word.")