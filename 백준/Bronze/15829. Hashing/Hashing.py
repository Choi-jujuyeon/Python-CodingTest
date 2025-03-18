a=int(input())
arr=list(input())

hash=0
p=1
for i in range(a):
    hash=(hash+(ord(arr[i])-ord('a')+1)*p)%1234567891
    p=(31*p)%1234567891
print(hash)