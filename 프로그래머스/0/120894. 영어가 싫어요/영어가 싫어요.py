def solution(numbers):
    for i,num in enumerate(["zero","one","two","three","four","five","six","seven","eight","nine"]):
        numbers=numbers.replace(num,str(i))
    return int(numbers)
    