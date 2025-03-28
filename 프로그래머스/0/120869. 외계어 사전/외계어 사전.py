def solution(spell, dic):
    num="".join(sorted(spell))
    for i in dic:
        if num==''.join(sorted(i)):
            return 1
    return 2