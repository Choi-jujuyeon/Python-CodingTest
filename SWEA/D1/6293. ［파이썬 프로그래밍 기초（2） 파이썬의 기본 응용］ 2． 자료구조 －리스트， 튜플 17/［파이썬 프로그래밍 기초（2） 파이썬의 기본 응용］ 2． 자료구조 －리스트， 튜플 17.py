arr=list(map(int,input().split(',')))
arr=[round(i*3.141592*2,2) for i in arr]
print(", ".join(map(str,arr)))
