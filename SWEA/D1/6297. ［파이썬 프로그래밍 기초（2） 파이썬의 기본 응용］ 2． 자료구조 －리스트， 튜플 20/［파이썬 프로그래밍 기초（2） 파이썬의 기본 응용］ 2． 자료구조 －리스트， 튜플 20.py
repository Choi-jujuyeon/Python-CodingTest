arr=list(map(int,input().strip().split(",")))
print(", ".join(map(str,[i for i in arr if i%2!=0])))