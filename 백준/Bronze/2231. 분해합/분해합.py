N=int(input())
for i in range(1,N):
    if (sum(int(j) for j in str(i))+i)==N:
        print(i)
        break
else:
    print(0)