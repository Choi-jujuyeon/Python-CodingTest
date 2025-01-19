arr=[]
marr=[]
for i in range(9):
    arr.append(list(map(int,input().split())))
    marr.append(max(arr[i]))
M=max(marr)
row=marr.index(M)
print(M)
print(row+1, arr[row].index(M)+1)