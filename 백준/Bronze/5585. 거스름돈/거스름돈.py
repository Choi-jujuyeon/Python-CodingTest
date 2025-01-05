a=int(input())
p=1000-a
count=0
arr=[500,100,50,10,5,1]

for i in arr:
    count+=p//i
    p%=i
print(count)