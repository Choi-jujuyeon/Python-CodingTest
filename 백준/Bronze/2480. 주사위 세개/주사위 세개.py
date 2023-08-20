from collections import Counter

a, b, c = map(int, input().split())
ct = Counter([a, b, c])

if a == b == c:
    print(10000+a*1000)
elif ct[a] >= 2 or ct[b] >= 2:
    if ct[a] >= 2:
        print(1000+a*100)
    else:
        print(1000+b*100)
else:
    print(max(a,b,c)*100)