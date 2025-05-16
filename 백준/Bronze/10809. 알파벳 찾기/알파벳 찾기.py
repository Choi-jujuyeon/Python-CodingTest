a=input()
r_arr=[-1]*26

for idx,ch in enumerate(a):
    if r_arr[ord(ch)-97]==-1:
        r_arr[ord(ch)-97]=idx
print(*r_arr)