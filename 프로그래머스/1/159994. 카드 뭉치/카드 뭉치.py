def solution(cards1, cards2, goal):
    lp,rp=0,0
    for i in goal:
        if lp < len(cards1) and cards1[lp]==i:
            lp+=1
        elif rp < len(cards2) and cards2[rp]==i:
            rp+=1
        else:
            return "No"
    return "Yes"
            
            
            