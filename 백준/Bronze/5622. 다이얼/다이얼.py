d={
    3:'ABC',
    4:'DEF',
    5:'GHI',
    6:'JKL',
    7:'MNO',
    8:'PQRS',
    9:'TUV',
    10:'WXYZ',
}
a=input()
sum=0
for i in a:
    for k,v in d.items():
        if i in v:
            sum+=k
print(sum)