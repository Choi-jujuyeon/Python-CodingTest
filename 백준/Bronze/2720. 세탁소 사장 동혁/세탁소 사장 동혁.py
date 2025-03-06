for _ in range(int(input())):
    i=int(input())
    q=i//25
    d= i%25//10
    n=i%25%10//5 
    p=i%25%10%5 
    print(q,d,n,p)