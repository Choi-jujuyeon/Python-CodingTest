a=input()
for i in range(ord('a'),ord('z')+1):
    ch=chr(i)
    if ch in a:
        print(a.index(ch),end=" ")
    else:
        print(-1, end=" ")
        