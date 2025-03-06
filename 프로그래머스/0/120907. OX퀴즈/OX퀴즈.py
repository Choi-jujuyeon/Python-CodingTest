def solution(quiz):
    a=[]
    for i in quiz:
        if eval(i.split("=")[0]) ==eval(i.split("=")[1]):
            a.append("O")
        else:
            a.append("X")
    return a