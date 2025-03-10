def solution(participant, completion):
    #문제의 핵심: 참가 못한 1명 찾기
    #Sort/Loop할 경우
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i]!=participant[i]:
            return participant[i] 
    return participant[-1]
        