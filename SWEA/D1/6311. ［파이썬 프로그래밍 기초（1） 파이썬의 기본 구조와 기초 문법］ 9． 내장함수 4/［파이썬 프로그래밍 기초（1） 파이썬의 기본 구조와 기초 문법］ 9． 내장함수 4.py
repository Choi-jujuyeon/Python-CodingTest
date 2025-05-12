a="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
s={'A':4, 'B': 3, 'C': 2, 'D':1}
s_arr=list(map(lambda x: s[x], a))
print(sum(s_arr))