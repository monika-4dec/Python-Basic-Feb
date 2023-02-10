#!/usr/bin/env python
# coding: utf-8
Build in functions

https://docs.python.org/3/library/functions.html

# In[1]:


## Function without any argument

def session():
    x=int(input("Number of people in session"))
    y=input("Name of session")
session()


# In[2]:


def details(name =" ", age=int):
    print("Name = %s Age = %d" %(name,age))
details("monika",25)


# In[19]:


def details (name=" ",age=int,job_role=""):
    #print("Name is %s age is %d and job role is %s"%(name,age,job_role))
    return name

details("A",32,"AC")


# In[4]:


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

# In[5]:


print(3+4)
print(6+8)
4


# In[6]:


def the(x,y):
    #print(x*y)
    return x
    
the(8,7)
the(4,5)


# # Different variable class can be passed within a function

# In[17]:


def Emp(name,age,g):
   print(name,age,g)

Emp("Rahul",20,"Male")


# In[21]:


def dex(*emp):
    print("The last employee is: " + emp[-1])
    
dex("Abc","ab12","er3")
#dex("A","B")
#dex ("ram","sam","lam","man")


# In[28]:


fruit=["kiwi","apple","pie","abc"]

def food(fruit):
    for i in fruit:
        print(i)

food(fruit)
    


# # Practice Questions on Functions
# Q Write a Python function to sum all the numbers in a list.

# In[33]:


def sum(numbers):
    total = 0
    for x in numbers:    
        total += x
    return total

sum((12,12))


# # Q Write a Python funtion to check whether a given number is the given range

# In[14]:


def test_range(n):
    if n in range(12,50):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(15)


# In[35]:


###  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
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


# In[ ]:


###  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0,"SPACES_":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test("PRACTICE More")

