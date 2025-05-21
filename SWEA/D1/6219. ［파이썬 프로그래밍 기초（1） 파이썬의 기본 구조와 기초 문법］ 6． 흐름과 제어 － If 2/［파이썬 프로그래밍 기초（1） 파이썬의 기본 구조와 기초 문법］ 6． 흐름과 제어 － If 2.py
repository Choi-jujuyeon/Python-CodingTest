a=int(input())
arr=[]
for i in range(1,a+1):
    if a%i==0:
        arr.append(i)
        print(f'{i}(은)는 {a}의 약수입니다.')
    if len(arr)==2:
        print(f'{a}(은)는 {arr[0]}과 {arr[-1]}로만 나눌 수 있는 소수입니다.')