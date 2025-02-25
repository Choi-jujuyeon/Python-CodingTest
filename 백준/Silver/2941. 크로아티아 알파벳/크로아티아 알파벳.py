a=['c=','c-','dz=','d-','lj','nj','s=','z=']

input=input()
for i in a:
    if i in input:
        input=input.replace(i,'x')
print (len(input))