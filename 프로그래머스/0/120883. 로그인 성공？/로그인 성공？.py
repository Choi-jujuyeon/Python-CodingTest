def solution(id_pw, db):
    for k,v in db:
        if id_pw[0] == k:
            if id_pw[1] == v:
                return "login"
            else:
                return "wrong pw"
    return "fail"