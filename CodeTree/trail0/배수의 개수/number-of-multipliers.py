arr = [int(input()) for _ in range(10)]
cnt1,cnt2=0,0
for i in arr:
    if i%3==0: cnt1 +=1
    if i%5==0: cnt2 +=1
print(cnt1,cnt2)
