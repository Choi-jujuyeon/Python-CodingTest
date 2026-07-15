arr=[ "apple", "banana", "grape", "blueberry", "orange"]

a=input()
cnt=0
for i in arr:
    if i[2]==a or i[3]==a:
        cnt+=1
        print(i)
print(cnt)