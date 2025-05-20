T=int(input())
for k in range(T):
    a=input()
    for i in a:
        if i in 'aeiou':
            a=a.replace(i,'')
    print(f'#{k+1} {a.strip()}')