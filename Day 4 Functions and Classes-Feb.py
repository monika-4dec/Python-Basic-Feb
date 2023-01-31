#!/usr/bin/env python
# coding: utf-8
Build in functions

https://docs.python.org/3/library/functions.html

# In[17]:


## Function without any argument

def session():
    x=int(input("Number of people in session"))
    y=input("Name of session")
session()


# In[18]:


def details(name =" ", age=int):
    print("Name = %s Age = %d" %(name,age))
details("monika",25)


# In[19]:


def details (name=" ",age=int,job_role=""):
    #print("Name is %s age is %d and job role is %s"%(name,age,job_role))
    return name

details("A",32,"AC")


# In[20]:


#Functions with Arguments
x=int(input("input first num= "))
y=int(input("input second num= "))
def cal(x,y):
    choice=input("Enter your choice( +,*,-,/)")
    if choice=="+":
        print("sum=",x+y)
    elif choice=="-":
        print("sub=",x-y)
    elif choice=="*":
        print("prod=",x*y)
    else:
        print("option not aviliable")
cal(x,y)


# In[ ]:


x = int(input("Enter 1st no.: "))
y = int(input("Enter 2nd no.: "))
 
def calci(x,y):
    choice = input("Enter your choice i.e. +,-,*,/")
    if choice == "+":
        print("Sum = ",x+y)
    elif choice == "-":
        print("Sub = ",x-y)
    elif choice == "*":
        print("Mul = ",x*y)
    elif choice == "/" and y !=0:
        print("Div = ",x/y)
    else:
        print("Invalid choice")
calci(x,y)


# # Return() is not mandatory in Python
# To let a function return a value, use the return statement:

# In[4]:


print(3+4)
print(6+8)
4


# In[7]:


def te(x,y):
    #print(x*y)
    return x
    
te(8,7)
te(4,5)


# # Different variable class can be passed within a function

# In[8]:


def Emp(name,age,f):
   print(name,age,f,sep="\t")

Emp("Monika",2,6)
Emp(1,2,3)


# In[10]:


def dex(*emp):
    print("The oldest employee is: " + emp[-1])
    
dex("Abc","ab12","er3")
dex("A","B")
dex ("ram","sam","lam","man")


# In[11]:


def food(fruit):
    for i in fruit:
        print(i)

fruit=["kiwi","apple","pie","abc"]

food(fruit)
    


# # Practice Questions on Functions
# Q Write a Python function to sum all the numbers in a list.

# In[9]:


def sum(numbers):
    total = 0
    for x in numbers:    
        total += x
    return total
#print(sum((12,34,55)))
sum((12,12))


# # Q Write a Python funtion to check whether a given number is the given range

# In[14]:


def test_range(n):
    if n in range(12,50):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(15)


# In[15]:


def breakdown():
    x= input("Enter a string")
    countupper = 0
    countlower = 0
    for i in x:
        if i.isupper():
                countupper+=1
        else:
                countlower+=1
    print(countupper, countlower)
breakdown()


# In[21]:


###  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0,"SPACES_":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test("PRACTICE More")


# # lambda - one line function which can take any number of arguments
# Lamba Function
# 
# The lambda keyword is used to create anonymous functions
# This function can have any number of arguments but only one expression, which is evaluated and returned.
# One is free to use lambda functions wherever function objects are required.
# You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.

# In[13]:


z= lambda a,b,c:a*b/c
z(8,9,3)


# In[16]:


## Create a lamba function that returns cube of a number.
z = lambda s:s*s*s
z(9)


# In[24]:


a=[2,4,-9,4,6,8,44,20,33]

even_list = list(filter(lambda x:(x%2 == 0),a))
even_list


# In[ ]:


z=[1,2,3,4]
x=list(map(lambda y:(y+2),z))
print(x)


# In[ ]:


##Lambda functions can take any number of arguments
x = lambda a, b,c : a**2+b*3+c
print(x(5, 6,7)) 


# # Write a Python program to sort a list of tuples using Lambda

# # The power of lambda is better shown when you use them as an anonymous function inside another function.

# In[27]:


def my(x):
    print(4*x)
my(3)


# In[ ]:


def myfunc(n):
  print("The number:",n)
  return lambda a : n**a
  
r = myfunc(2)

print(r(3))


# In[ ]:


def mydata(n):
  return lambda a,b:(a+b)*n
var = mydata(4)
print(var(2,3))


# # Date Time Module

# In[32]:


## Time Module:
from time import time, ctime
t = time()

ctime(t)## for current time


# In[33]:


import time
current_local = time.localtime()
current_local.tm_zone


# In[34]:


import time
a=time.strftime('%m-%y-%d', time.localtime())

t = time.strftime("%d/%m/%y|%H:%M:%S")
print (a)
print(t)


# In[35]:


## %%time 

import time 
## Provide delay in a program
print("Hi")
time.sleep(2)
print("Welcome")


# In[36]:


print(time.strftime("%y/%m/%d|%H:%M:%S"))


# In[37]:


Tstr=time.strftime("%A/%B|%a/%b") # Day|MONTH
print(Tstr)
tstr=time.strftime("%H:%M:%p")# Current time IN AM/PM
print(tstr)
w=time.strftime("%z")
print(w)


# In[38]:


import datetime 
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))#%b
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))


# In[39]:


## Python code to check time of execution of a program 
# starting time
start = time.time()

# program body starts
for i in range(10):
    print(i)

# sleeping for 1 sec to get 10 sec runtime
time.sleep(1)

# program body ends

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")


# # Classes in Python &OO programming

# In[40]:


class  Program1:
    "HI"   
#print(Program1)#Tell about status of class.
Program1


# In[41]:


class Program1:
    name="RAM"
    age = 29
print("NAME is %s and age is %d"%(Program1.name,Program1.age))


# In[42]:


# Create a class name mobile store, Price=0.0,Type="",Brand, Three 
class empdetails:
    name="RAM"
    age = 29
Emp1= empdetails()
Emp2 = empdetails()

Emp1.name ="A"
Emp1.age = 9
Emp2.name = "B"
Emp2.age = 32    
#print(" %s   %d "%(Emp1.name,Emp1.age))
#print(" %s   %d "%(Emp2.name,Emp2.age))
for x in range(1,3):
        print(eval("Emp%d.name"%(x)), eval("Emp%d.age"%(x)))


# # - self is used to represent the instance of the class. With this keyword, you can access the attributes and methods class in python. it helps to bind attributes with the given arguments.
# - In Python we have methods that make the intance to be passed automatically, but not received automatically.

# In[ ]:


class X:
    "Classses and functions"
    myroll= 9
    def  student(self):
        print('This is Science Class')
rani = X()
print(X.student)
print(rani.student)
rani.student()


# In[ ]:


class Y:
     a = 9
     b = 3.3
     c = 23.4
     d = 0.0
     def details(r):
        r.c= r.a * r.b 
        r.d = r.a/r.b
        t=round(r.d,3)
        print(r.c,t,sep=",")
cal1=Y()
cal2= Y()
cal1.a=5
cal1.b=4.7
cal1.details()


# In[ ]:


### Class and Function


class Shop:
        "Things in MYshop"
        Quantity = 10
        Type       =   ""
        price=500.00
        def bill(self):
            print("your bill for  % s dress of %d quantity is %drs:"%(self.Type,self.Quantity,self.price))
coustmer1=Shop()
coustmer1.Quantity=5
coustmer1.Type="saree"
coustmer1.price=20000
coustmer1.bill()
print(50*"*")


# In[ ]:


# dictionary from an class's fields.
class dObj():
     def __init__(self):
         self.x = 'age'
         self.y = 'name'
         self.z = 'Gender'
     def do(self):
         pass
d = dObj()
print(d.__dict__)


# # WHILE LOOP

# In[ ]:




