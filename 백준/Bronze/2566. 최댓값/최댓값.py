arr=[]
for _ in range(9):
    row=list(map(int,input().split()))
    arr.append(row)
    
maxVal=-1
maxR, maxC = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > maxVal:
            maxVal = arr[i][j]
            maxR=i+1
            maxC=j+1
print(maxVal)        
print(maxR,maxC)