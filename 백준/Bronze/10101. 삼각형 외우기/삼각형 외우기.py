a=[int(input()) for i in range(3)]
if sum(a)!=180:
    print("Error")
elif len(set(a))==1:
    print("Equilateral")
elif len(set(a))==2:
    print("Isosceles")
else:
    print("Scalene")