def solution(people, limit):
    lp,rp=0,len(people)-1
    people.sort()
    boat=0
    while lp<=rp:
        if people[lp] +people[rp] <=limit:
            lp+=1
        rp-=1
        boat+=1
    return boat
        