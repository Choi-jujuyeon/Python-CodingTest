def solution(hp):
    result=0
    if hp>=5:
        result=hp//5
        hp%=5
    if hp>=3:
        result+=hp//3
        hp%=3
    if hp<=2:
        result+=hp
            
    return result
            