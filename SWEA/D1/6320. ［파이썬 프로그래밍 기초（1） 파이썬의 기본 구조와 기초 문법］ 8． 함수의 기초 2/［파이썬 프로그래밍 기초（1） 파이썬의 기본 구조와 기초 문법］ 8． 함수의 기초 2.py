a=input()
b=input()
ap=input()
bp=input()
def play(p1,p2):
    if p1=="가위":
        if p2=="바위":
            print("바위가 이겼습니다!")
        elif p2=="보":
            print("가위가 이겼습니다!")
        else:
            print("비겼습니다!")
    
    elif p1 =="바위":
        if p2=="바위":
            print("비겼습니다!")
       	elif p2 =="보":
            print("보가 이겼습니다!")
    elif p1 =="보":
        if p2=="보":
            print("비겼습니다!")

play(ap,bp)
    