def solution(sizes):
    #큰걸 항상 가로로 보내기
    mw,mh=0,0
    for w,h in sizes:
        if h>w:
            w,h=h,w
        mw=max(mw,w)
        mh=max(mh,h)
    return mw*mh
        
        
        