def test(w):
    for i in range(int(len(a)//2)):
        if a[i]!=a[-i-1]:
            return False
    return True
a=input()
if test(a):
    print(a)
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print(a)
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")