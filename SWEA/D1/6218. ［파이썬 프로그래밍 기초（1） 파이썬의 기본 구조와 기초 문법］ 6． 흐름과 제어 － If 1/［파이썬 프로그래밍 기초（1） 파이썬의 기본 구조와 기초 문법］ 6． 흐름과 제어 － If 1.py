a=int(input())
print(*[f'{i}(은)는 {a}의 약수입니다.' for i in range(1,a+1) if a%i==0], sep='\n')