def solution(phone_book):
    hashDict={}
    for i in phone_book:
        hashDict[i]=1
    
    for i in phone_book:
        jj=''
        for j in i:
            jj+=j
            if jj in hashDict and jj!=i:
                return False
    return True
        