def play(a,b):
    if dic[a]=="가위":
        if dic[b]=="바위":
            print('B')
        else:
            print('A')
    elif dic[a]=="바위":
        if dic[b] =="가위":
            print('A')
        else:
            print('B')
    elif dic[a]=="보":
        if dic[b] =="가위":
            print('B')
        else:
            print('A')
dic={1:'가위',2:"바위",3:"보"}
a,b=map(int,input().split())
play(a,b)