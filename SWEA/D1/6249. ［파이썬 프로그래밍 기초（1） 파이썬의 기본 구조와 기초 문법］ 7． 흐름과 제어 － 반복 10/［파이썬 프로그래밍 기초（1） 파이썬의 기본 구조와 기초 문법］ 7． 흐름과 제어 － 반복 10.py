a=input()
arr=[0]*10
for i in a:
    arr[int(i)]+=1
print("0 1 2 3 4 5 6 7 8 9")
print(*arr)