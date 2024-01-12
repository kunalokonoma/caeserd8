'''
import math

def paint(h,w,c):
    cdk=h*w/c
    cd=math.floor(cdk)
    print(cd)



x=int(input("enter "))
z=int(input("enter "))
y=int(input("enter "))

paint(x,y,z)
'''
'''

def prime(number):
    for n in range(2,number):
        if number%n==0:
            iz="false"
            break
        else:
            iz="true"
    print(iz)

a=int(input("enter "))

prime(a)
'''

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




'''
def encode(txt,no):
    pop=""
    no=int(no)
    for i in txt:
        numb=alphabets.index(i)
        np=numb+no
        op=alphabets[np]
        pop=pop+op
    print(pop)
            

def decode(txt,no):
    pop=""
    for i in txt:
        numb=alphabets.index(i)
        np=numb-no
        op=alphabets[np]
        pop=pop+op
    print(pop)
    

def need(d):
    if direction=="d":
        decode(text,number)
    elif direction=="e":
        encode(text,number) 
'''       

'''
def ceaser():
    
    
    
    dir=input("enter d or e ")
    txt=input("enter message ")
    no=int(input("enter shift "))
    
    if dir=='d':
        pop=""
        for i in txt:
            numb=alphabets.index(i)
            np=numb-no
            op=alphabets[np]
            pop=pop+op
        print(pop)
        
    elif dir=='e':
        pop=""
        no=int(no)
        for i in txt:
            numb=alphabets.index(i)
            np=numb+no
            op=alphabets[np]
            pop=pop+op
        print(pop)
        
ceaser()



'''
def ceaser():
    
    
    
    dir=input("enter d or e ")
    txt=input("enter message ")
    no=int(input("enter shift "))
    
    no=no%26  
    
    if dir=='d':
        pop=""
        for i in txt:
            if i not in alphabets:
                op=i
            else:
                numb=alphabets.index(i)
                np=numb-no
                op=alphabets[np]
            pop=pop+op
        print(pop)
        
    elif dir=='e':
        pop=""
        no=int(no)
        for i in txt:
            if i not in alphabets:
                op=i
            else:
                numb=alphabets.index(i)
                np=numb-no
                op=alphabets[np]
            pop=pop+op
        print(pop)

ceaser()     

    
        

