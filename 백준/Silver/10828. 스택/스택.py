import sys
T=int(input())
a=[]
for line in sys.stdin:
    cmd=line.strip()
    
    if "push" in cmd:
        _,num=cmd.split()
        a.append(int(num))
    elif "pop" in cmd:
        print(a.pop() if a else -1)
    elif "size" in cmd:
        print(len(a))
    elif "empty" in cmd:
        print(0 if a else 1)
    elif "top" in cmd:
        print(a[-1] if a else -1)