def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    days=sum(month[:a-1]) + b -1
    return day[days%7]