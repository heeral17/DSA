#Docstring for Maths
from math import sqrt

'''
1 Extarction of digits 

def ext(n):
    while n>0:
        e=n%10
        print(e,end=" ")
        n=n//10
n=int(input("Enter a no: "))
ext(n)


#2 Count Digits
def count(n):
    ct=0
    while n>0:
        c=n%10
        ct+=1
        n=n//10
    print(ct)
n=int(input("enter a no: "))
count(n)        



#3.Armstrong no
def arms(n):
    org=n
    sum=0
    digit=len(str(org))
    while n>0:
        k=n%10
        sum=sum+(k**(digit))
        n=n//10

    if org==sum:
        print("It is Armstrong!!")
    elif n<0:
        print("NT for negative no")
    else:
        print("NOT") 
n=int(input("ENter a no."))
arms(n)


#4 Reverse no

def rev(n):
    rev=0
    while n>0:
        k=n%10
        rev=(10*rev)+k
        n=n//10

    print(f"Reversed no is :{rev}" )

n=int(input("Enter the original no"))   
rev(n)     


#5 Palindrome 
def pali(n):
    org=n
    rev=0
    while n>0:
        k=n%10
        rev=(10*rev)+k
        n=n//10

    if org==rev:
        print("Palindrome !") 
    else:
        print("oops)(")

n=int(input("enter the no: "))          
pali(n)



#6 Factors 
def factors(n):
    fact=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            fact.append(i)
            if n//i!=i:
                fact.append(n//i)
    fact.sort()
    print(fact)
n=int(input("enter the no "))            
factors(n)


#7 Fibonacci

def fibo(n):
    sum,a,b=0,0,1
    for i in range(n):
        sum=a+b
        a,b=b,sum
    print(sum)

n=int(input("enter the NO"))        
fibo(n)


#8 factorial
def fact(n):
    multiply=1
    for i in range(1,n+1):
        multiply=multiply*i  

    print(multiply)
n=int(input("enter ::"))    
fact(n)


#9 Prime 

def prime(n):

    if n<2:
        print("NOT PRIME ")
    for i in range(2,int(sqrt(n))+1):
        if n%i==0 :
            print('NOT a prime')
            return 
    print("Its  a PRIME NO ")

n=int(input("enter the no"))
prime(n)


'''
#10 Perfect square

def sq(n):
    if n//sqrt(n)==sqrt(n):
        print("perfect")
    else:
        print("not")

n=int(input("no   pls"))
sq(n)