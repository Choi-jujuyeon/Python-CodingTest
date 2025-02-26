def solution(code):
    mode=0
    arr=[]
    for i in range(len(code)):
        if mode==0:
            if code[i]!='1' and i%2==0:
                arr.append(code[i])
            elif code[i]=='1':
                mode=1
        else:
            if code[i]!='1' and i%2==1:
                arr.append(code[i])
            elif code[i]=='1':
                mode=0
    return "".join(arr) if arr else "EMPTY"
            
            
        