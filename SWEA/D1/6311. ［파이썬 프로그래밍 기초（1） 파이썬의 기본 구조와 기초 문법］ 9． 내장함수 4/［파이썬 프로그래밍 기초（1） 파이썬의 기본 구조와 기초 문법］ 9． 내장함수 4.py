from collections import Counter
a="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
result=0

for k,v in Counter(a).items():
    if k=="A":
        result+=v*4
    elif k=='B':
        result+=v*3
    elif k=='C':
        result+=v*2
    else:
        result+=v*1
print(result)