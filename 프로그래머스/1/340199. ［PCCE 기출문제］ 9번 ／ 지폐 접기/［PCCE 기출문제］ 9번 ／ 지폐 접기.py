def solution(wallet, bill):
    count=0
    while max(wallet)<max(bill) or min(wallet)<min(bill):
        if bill[0]>bill[1]:
            bill[0]//=2
        else:
            bill[1]//=2
        count+=1
    return count