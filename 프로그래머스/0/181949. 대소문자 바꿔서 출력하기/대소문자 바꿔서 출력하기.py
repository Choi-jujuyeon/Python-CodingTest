str = input()
for i in str:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")
