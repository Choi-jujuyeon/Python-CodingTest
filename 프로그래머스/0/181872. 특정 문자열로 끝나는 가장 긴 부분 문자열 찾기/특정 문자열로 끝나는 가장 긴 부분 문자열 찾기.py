def solution(myString, pat):
    a=[i for i in range(len(myString)) if pat in myString[i:len(pat)+i]]
    return myString[:a[-1]+len(pat)]