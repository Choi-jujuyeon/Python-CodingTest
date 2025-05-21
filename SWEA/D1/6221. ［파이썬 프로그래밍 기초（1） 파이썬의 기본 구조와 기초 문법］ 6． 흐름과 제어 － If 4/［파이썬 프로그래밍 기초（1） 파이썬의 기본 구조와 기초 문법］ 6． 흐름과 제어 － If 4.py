arr = ['가위', '바위', '보']

m1 = input()
m2 = input()

if m1 == m2:
    print("Result : Draw")
elif (m1 == '가위' and m2 == '보') or (m1 == '바위' and m2 == '가위') or (m1 == '보' and m2 == '바위'):
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")
