def solution(score):
    a = sorted([[idx, sum(num)] for idx, num in enumerate(score)], key=lambda x: x[1], reverse=True)

    # 결과값 저장할 배열
    b = [0] * len(score)
    rank = 1  # 등수
    prev = a[0][1]  # 첫 번째 점수를 기준으로 초기화

    for i, (idx, num) in enumerate(a):  # ✅ enumerate() 추가 (정렬된 리스트에서의 인덱스)
        if i > 0 and num != prev:  # ✅ 첫 번째는 비교하지 않도록 i > 0 조건 추가
            rank = i + 1  # ✅ 현재 인덱스(i) 기반으로 등수 갱신
        
        b[idx] = rank  # ✅ 원래 위치에 등수 저장
        prev = num  # ✅ 이전 점수 업데이트

    return b
