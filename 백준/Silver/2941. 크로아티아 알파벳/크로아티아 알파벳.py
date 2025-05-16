arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
a=input()
for i in arr:
    if i in a:
        a=a.replace(i,'A')
print(len(a))