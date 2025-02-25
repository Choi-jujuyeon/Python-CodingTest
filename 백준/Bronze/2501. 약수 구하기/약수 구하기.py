a,b=map(int,input().split())
arr=sorted([i for i in range(1,a+1) if a%i==0])
print (arr[b-1] if b<=len(arr) else 0)