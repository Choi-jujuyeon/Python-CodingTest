count = 0
n=int(input())

def fac(num):
    global count

    if num == 0 or num == 1:
        return 1
    count += 1
    result = num * fac(num - 1)
    if count == n:
        print(result)
    return result


print(fac(n))