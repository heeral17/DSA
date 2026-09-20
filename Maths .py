'''
class node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
        
class singlell:
    def __init__(self,head=None):
        self.head=head
     
    def inEnd(self,value):
        temp=node(value)
        if self.head!=None:
            t1=self.head
            while temp.next!=None:
                t=t1.next
            t1.next=temp
        else:
            self.head=temp
            
    
    def Beg(self,value):
        temp=node(value)
        temp.next=self.head
        self.head=temp
        
    def mid(self,value,x):
        temp=node(value)
        t1=self.head
        while (t1.next!=None):
            if t1.data==x:
                temp.next=t1.next
                t1.next=temp
            else:
                t1=t1.next        
            
    def pr(self):
        t1=self.head
        while t1.next!=None:
            print(t1.data)
            t1=t1.next                           
        print(t1.data)        
                
ob=singlell()
ob.inEnd(30)
ob.inEnd(10)
ob.mid(25,30)
ob.beg(6)
ob.pr()
                
                



##1.) Extraction of Digits 

n=int(input("Enter number  :"))
while n>0:
    last_digit=n%10
    print(last_digit)
    n=n//10

    
## 2.)Count Digit 
n=int(input("Enter no "))
count=0
while n>0:
    last_digit=n%10
    count=count+1
    n=n//10
print(count)    

'''

## 3 ) Palindrome 
def pali(n):
    original=n
    rev_no=0
    while n>0:
        last_digit=n%10 
        rev_no=rev_no*10+last_digit
        n=n//10

    if original==rev_no:
        print("palindrome")
    else:
        print("not")

n=int(input("Check:"))
pali(n)

