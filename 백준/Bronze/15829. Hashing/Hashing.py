n=int(input())
arr=[ord(i)-ord('a')+1 for i in list(input())]
sum=0
for i in range(len(arr)):
    sum+=arr[i]*31**(i)
print(sum)