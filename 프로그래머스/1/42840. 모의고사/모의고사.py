def solution(answers):
    arr = [
        [1, 2, 3, 4, 5],                
        [2, 1, 2, 3, 2, 4, 2, 5],       
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  
    ]
    
    res = []
    for num in arr:
        count = 0
        for i in range(len(answers)):
            if answers[i] == num[i % len(num)]:
                count += 1
        res.append(count)

    max_score = max(res)
    answer = []

    for i in range(len(res)):
        if res[i] == max_score:
            answer.append(i + 1)

    return answer
