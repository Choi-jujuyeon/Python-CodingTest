a = []
for i in range(5):
    a.append(input())

maxRow = max(len(row) for row in a)

for i in range(maxRow):
    for j in range(5):
        if i < len(a[j]):  
            print(a[j][i], end="")
