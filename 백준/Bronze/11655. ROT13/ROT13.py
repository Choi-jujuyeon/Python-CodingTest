low=[i for i in range(ord('a'), ord('z')+1)]*2
up=[i for i in range(ord('A'), ord('Z')+1)]*2

ch=input()
a=[]
for i in ch:
    if ord(i) in low:
        a.append(chr(low[ord(i)-ord('a')+13]))
    elif ord(i) in up:
        a.append(chr(up[ord(i)-ord('A')+13]))
    elif i.isdigit():
        a.append(i)
    else:
        a.append(" ")
print("".join(a))