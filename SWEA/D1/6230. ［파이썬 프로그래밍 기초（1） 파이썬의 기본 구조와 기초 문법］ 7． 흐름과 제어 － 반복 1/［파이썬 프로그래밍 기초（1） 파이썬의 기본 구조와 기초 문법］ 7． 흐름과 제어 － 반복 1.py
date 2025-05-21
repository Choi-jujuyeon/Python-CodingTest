arr=[88,30,61,55,95]
for i in range(len(arr)):
    if arr[i]>=60:
        re='합격'
    else:
        re='불합격'
    print(f'{i+1}번 학생은 {arr[i]}점으로 {re}입니다.')