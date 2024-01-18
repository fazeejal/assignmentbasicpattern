
# a

for i in range(4):
    for j in range(i):
        print("*",end=" ")
    print()

##b

x=4
num=1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()

   ###e
     
x=4
num=2
for i in range(1,x+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+2
    print()

##c
for i in range(65,70):
    k=i
    for j in range(65,i+1):
        print(chr(k), end=" ")
        k=k+1
    print()


###d
    
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j), end=" ")
        
    print()