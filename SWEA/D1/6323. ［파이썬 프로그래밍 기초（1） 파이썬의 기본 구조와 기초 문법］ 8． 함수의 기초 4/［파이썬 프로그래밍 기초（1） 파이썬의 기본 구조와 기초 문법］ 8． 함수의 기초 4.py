a=int(input())
arr=[1]*a
for i in range(2,a):
    arr[i]=arr[i-1]+arr[i-2]
print(arr)