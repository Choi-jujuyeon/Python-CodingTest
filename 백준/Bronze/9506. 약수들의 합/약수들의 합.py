while True:
    a=int(input())    
    if a==-1:
        break
    arr=[i for i in range(1,a) if a%i==0]           
    if sum(arr)==a:
        print(f'{a} = {' + '.join(map(str, arr))}')
    else:
        print(f'{a} is NOT perfect.')