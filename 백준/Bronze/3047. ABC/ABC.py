arr=list(map(int,input().split()))
arr.sort()

o1,o2,o3=input()

print(arr[ord(o1)-ord("A")],arr[ord(o2)-ord("A")],arr[ord(o3)-ord("A")])