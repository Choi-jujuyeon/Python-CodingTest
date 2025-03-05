def solution(numbers):
    for v,k in [
        ("1", "one"), ("2", "two"), ("3", "three"),
        ("4", "four"), ("5", "five"), ("6", "six"),
        ("7", "seven"), ("8", "eight"), ("9", "nine"),("0","zero")
    ]:
        numbers=numbers.replace(k,str(v))
    return int(numbers)