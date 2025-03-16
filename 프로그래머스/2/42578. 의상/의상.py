def solution(clothes):
    #1.옷을 종류 별로 구분한다
    hash_map={}
    for cloth,type in clothes:
        hash_map[type]=hash_map.get(type,0)+1
    print(hash_map)
     
    #2.입지 않는 경우를 추가하여 모든 조합을 계산한다.
    result=1
    for type in hash_map:
        result*=(hash_map[type]+1)
        
    #3.아무 종류의 옷도 입지 않는 경우를 제외한다
    return result-1
    