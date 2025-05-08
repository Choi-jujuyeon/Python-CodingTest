from collections import Counter
a=1
for _ in range(3):
    a*=int(input())
# print(Counter(str(a))[str(i)])
for i in range(0,10):
    if str(i) in Counter(str(a)):
        print(Counter(str(a))[str(i)])
    else:
        print(0)