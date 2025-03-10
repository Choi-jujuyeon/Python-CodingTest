def solution(participant, completion):
    #문제의 핵심: 참가 못한 1명 찾기
    #Hash 사용
    
    #01.participant hash sum
    hashDict={}
    sumHash=0
    for i in participant:
        h=hash(i)
        hashDict[h]=i
        sumHash+=h
    
    #02.completion hash 차이
    for i in completion:
        sumHash-=hash(i)
        
    #03.남은 값 
    return hashDict[sumHash]
    
    