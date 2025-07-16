def solution(brown, yellow):
    ss=brown + yellow
    for h in range(3,int(ss**0.5)+1):
        if ss%h==0:
            w=ss//h
            if (w-2) * (h-2) == yellow:
                return [w,h]