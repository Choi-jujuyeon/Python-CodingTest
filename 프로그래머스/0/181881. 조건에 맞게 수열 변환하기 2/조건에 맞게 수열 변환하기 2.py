def solution(arr):
    count = 0
    prev = []
    
    while arr != prev:  
        prev = arr[:]  
        for index in range(len(arr)):
            if arr[index] >= 50 and arr[index] % 2 == 0:
                arr[index] //= 2
            elif arr[index] < 50 and arr[index] % 2 == 1:
                arr[index] = arr[index] * 2 + 1
        count += 1
    
    return count-1
