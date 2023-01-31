#!/usr/bin/env python
# coding: utf-8

# ### Day 1
# - 1. [Using Interpreter](#section1)</br>
#     - 1.1 [ Python's Interactive Prompt](#section101)<br/>
#     - 1.2 [ Scripting](#section102)<br/>
#     - 1.3 [Program Execution Model](#section103)<br/>
#     - 1.4 [Program Architecture: modules](#section104)<br/>
#     - 1.5 [How to run Python program](#section105)<br/>
#     - 1.6 [Quick Intro Anaconda & Jupiter Notebook(IDLES)](#section106)<br/>
#     

# <a id=sectio></f>  
# ## What is python and why it is so popular ?
# 

# 
# Python is one among the most popular dynamic programming languages that is being used today. Python is an open-source and object-oriented programming language developed by Dutchman Guido van Possum in 1980s. This language can be utilized for a wide range of applications like scripting, developing and testing.  Due to its elegance and simplicity, top technology organizations like Dropbox, Google, Quora, Mozilla, Hewlett-Packard, Qualcomm, IBM, and Cisco have implemented Python.
# 
# 
# ![image.png](attachment:image.png)
# 
# Several websites state that Python is one among the most famous programming language of 2016. Because of its implementation and syntax, it pressures more on code readability. When compared to other programming languages like C++ and Java, it requires the programmer to develop lesser codes. It offers automatic memory management and several standard libraries for the programmer. Once a programmer completes Python certification training, he can gain knowledge and experience in a wide range of top IT organizations. It is a general-purpose and high-level coding language.
# 
# Because of its features, a large number of programmers across the world, showing interest in making use of this language to develop websites, GUI applications, and mobile applications. The main reason that brings Python one among the top coding languages is that it allows the developers to figure out the concepts by developing readable and less code. Several advantages of Python supports the programmers to alleviate the effort as well as the time required for developing complex and large applications.

# <a id=section1></f>  
# ## 1. Using the Interpreter
# 
# ![image.png](attachment:image.png)
# 
# 

# **Interpreter** : An interpreter is a program that reads and executes code. This includes source code, pre-compiled code, and scripts. So if we talk about python interpreter it will execute the code in pytyhon by taking single code line at a time.
# 
# **Scripting** : Any program written in python is called a script.The interpreter reads and executes each line of code one at a time, just like a SCRIPT for a play or an audition, hence the the term "scripting language". Python uses an interpreter to translate and run its code and that's why it's called a **scripting language**
# 
# ### Python Program Executing Model & Architecture
# 
# A Python program is constructed from code blocks. A block is a piece of Python program text that is executed as a unit. The following are blocks: a module, a function body, and a class definition. Each command typed interactively is a block. A script file (a file given as standard input to the interpreter or specified as a command line argument to the interpreter) is a code block. A script command (a command specified on the interpreter command line with the -c option) is a code block. The string argument passed to the built-in functions eval() and exec() is a code block.
# 
# A code block is executed in an execution frame. A frame contains some administrative information (used for debugging) and determines where and how execution continues after the code block’s execution has completed.
# 
# ![image.png](attachment:image.png)
# 
# - A scope defines the visibility of a name within a block. If a local variable is defined in a block, its scope includes that block. If the definition occurs in a function block, the scope extends to any blocks contained within the defining one, unless a contained block introduces a different binding for the name.
# 
# ## Run a Python Program
# a=10
# In[48]:


h=15
print(h)


# In[53]:


x=9
y="monika"
z=14.5
print(x,y)
print(x,y,z)
#print(x,y,z)
print(y,x,z, sep="\t")


# In[57]:


a="2"
b="3"
print(type(a))
print(type(b))
c=a+b # concatenating a and b
print(type(c))


# ## Installation
# 
# The following link provides the complete installation guide for python basic IDLE 
# 
# https://www.python.org/downloads/

# ## Anaconda & Jupyter notebook
# 
# Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment. Package versions are managed by the package management system conda.The Anaconda distribution is used by over **13 million** users and includes more than **1400** popular **data-science** packages suitable for Windows, Linux, and MacOS.
# 
# ![image.png](attachment:image.png)
# 
# The following link will guide you to anaconda interface and download details:
# https://www.anaconda.com/

# ### Day 1
# - 2. [. Python Scripting (2hrs)](#section2)</br>
#     - 1.1 [ Introduction](#section201)<br/>
#     - 1.2 [Sequence types & Assignments](#section106)<br/>
#     - 1.3 [List Iteration](#section106)<br/>
#     - 1.4 [Mutable Vs Immutable Objects](#section106)<br/>
#     - 1.5 [Membership Statements](#section106)<br/>
#     - 1.6 [Multi Target Assignment](#section106)<br/>
#     

# In[58]:


# The Python Variable Function
x=9
y="monika"
z=12
#print(x,y,z) Shortcut: Ctrl+/
print(y,x,z, sep="\t")


# In[59]:


## %s-strings,%d-int,%f-decimal
print("%s is %d years old and her height = %f inches" %(y,x,z))


# In[61]:


#type function
type(12),type(18.6),type("monika"),type(-13),type(-14.0),type("b"),type("&"),type("67A")


# In[63]:


##Type Casting
print(float(18))
print(int(13.7))
str(8.9)
int("13")
int(13.5)


# ## INDENTATION

# In[ ]:


##Variable Decalartion
t=9
x,y,z=1,"a",14.5
a_1= 9
print(a_1)
x


# In[70]:


t=9
v=6
y_h=t+v
w=54
#indentation error discussion


# ## Input 

# # Coding Exercise: the output should be like:-

# In[ ]:


#Day 1 - String Manipulation
#String Concatenation is done with the "+" sign.
#e.g. print("Hello " + "world")
#New lines can be created with a backslash and n. -->


# # The Python Input Function and new line

# In[71]:


print("monika")
print("arora")


# In[72]:


print("monika arora")


# In[75]:


a="monika"
b="arora"
print(a+" "+b)


# In[81]:


input("Name?\n")


# In[76]:


print("What is your name?")
a=input("What is your name?")
a
b=input("What is your name?\n")


# In[ ]:


print("Hello"+input('What is your name?'))


# In[ ]:


## name = str, age = int ,years of exper = float
name=input(" Enter your Name: ")
age=int(input("Age:"))
exp=float(input("Job exp in years:"))
print("your details are:")
print("Name = %s" %(name))


# # The Python len Function

# In[ ]:


a=[1,2,3]
len(a)


# # Exercise: Write a program that prints the number of characters in a user's name.

# In[ ]:


# a=input("What is your name?")
# len(a)


# # Exercise: Write a program that prints the number of characters in a user's name.
#  If a hold 5 and b holds 6, then it should print a= 6 and b= 5

# In[ ]:


a=5
b=6
c=a
a=b
b=c
print("a=",a)
print("b=",b)


# # PROJECT

# In[ ]:


# "Welcome to the Band Name Generator."
# "What's the name of the city you grew up in?
# Noida
# "What's your pet's name?
# Frosty
# "Your band name could be Noida Frosty


# In[ ]:


print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)


# ## Built-in Types
# Approximately two dozen types are built into the Python interpreter and grouped into a few major categories, as shown :
# ![image.png](attachment:image.png)

# ## Data Types

# In[ ]:


len("Hello")
#print(len(12345)) # This will give error because we need to understand about data types
# Data Types
# string
print("Hello"[0]) # Find the last character?
a=123

b="123"

c=123.23

d=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#now print 123456?


# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # Exercise: 
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# In[ ]:


number=input("enter a two digit number")
first_digit = int(number[0])
second_digit = int(number[1])

#Add the two digits together
output = first_digit + second_digit

print(output)


# # Mathematical Operators

# In[ ]:


x=9
x*x+2*x-6
2*3 #2 times 3
2**3 #2 to the power 3


# In[ ]:


#PEMDAS:= (),**,*,/,+,-
print(3*3+3/3-3)
print(3*(3+3/3-3))


# In[ ]:


6/3 # Gives a floating point number


# In[ ]:


print(round(23/8,3))


# In[ ]:


## Numbers 
3+4
3-8
4*5
3**4
14/3 
12//3
14%3


# # Code Challenge
# BMI Calculator: https://app.codingrooms.com/w/26NvYLliNdNo

# In[ ]:


height = input("enter your height in ft: ")
weight = input("enter your weight in kg: ")


weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)


# ## Conditional
# ## if / else
# 
 if condition:
    do this
else:
    do this
# In[ ]:


water_level=50;
#water_level=int(input("the water level is"));
if water_level>80:
    print("Drain water")
else:
    print("Continue")


# In[ ]:


# Roller Coaster ride

print("Welcome to the rollercoater ride")
height=int(input("What is your height?"))

if height>120:
    print("You can ride")
else:
    print("You have to grow taller before you take a ride :)")


# # Comparison Operators
# 
# # assigning values : =
# # equality: ==

# In[ ]:


# Roller Coaster ride

print("Welcome to the rollercoater ride")
height=int(input("What is your height?"))

if height==120:
    print("You can ride")
else:
    print("You have to grow taller before you take a ride :)")

Instructions
Write a program that works out whether if a given number is an odd or even number.

(Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.)
# In[ ]:


a=int(input("Enter a Number"))
if a%2==0:
    print("Its an Even Number")
else:
    print("Its an odd number")

Nested If statement

if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this

# In[20]:


a=int(input("enter the height"))
w=int(input("enter your weight"))
if a>120:
    if 50<w<70:
        print("The ticket price is Rs 120")
    else:
        print("The ticket price is Rs 200")
else:
    print("You cant buy the ticket")

if/elif/else

if condition 1:
    do A
elif condition 2:
    do B
else:
    do this
    
    
Example:
For under 12 years: The price of the ticket should be $12
For 12 -18 years: The price of the ticket should be $50
For Over 18 years: The rpice of the ticket should be $100
But this is applied only to those whose height is more than 120 cms
# In[21]:


a=int(input("enter the height"))
age=int(input("enter your age"))
if a>120 or a==120:
    if age<12 or age==12:
        print("Pay $12")
    elif 12<age<18:
        print("Pay $50")
    elif age>18:
        print("Pay $100")
else:
    print("Sorry! No rides for now")


# ## Sequence type & Assignment
# - Sequences represent ordered sets of objects indexed by nonnegative integers and include strings, Unicode strings, lists, and tuples. -Strings are sequences of characters -
# - lists and tuples are sequences of arbitrary Python objects. 
# - Strings and tuples are immutable; lists allow insertion, deletion, and substitution of elements.
# - All sequences support iteration.

# ## Strings

# In[22]:


x1=1234
x2=1234
#print(x1+x2)
x="data"
#print(x+x)
len(x)
#x[-1]
#"as12"-aplha numeric
#"1234"-num
#"abc"-
a="4#%&"
b=" 4#%&"


# In[23]:


print('hello') #single quotes
print("hello") #double quotes
print("hello\nmonika") # next line
print("hello"+"monika")
# add a space in between hello and monika


# In[24]:


c=" 12"
c.isspace()


# In[25]:


x="DATA"
x.upper()


# In[26]:


x="data"
x.capitalize()
x.casefold()
z=x.encode()
x.isalnum()
x.isalpha()
x.isascii()
x.isdecimal()
x.isspace()
x.join("a")


# In[27]:


a="Python is a data science tool"
b="1234"
print("This is concading=",a+b)
print("Length of string a =",len(a)) #len() for finding length
print(a.isupper())# checks upper case
print(b.islower())# checks lower case
c=a.upper()
print("Converting a into uppercase=",c)
d=b.capitalize()
print(d)


# ## Indexing 
b="abc12334"
print(b[0]) # Start
print(b[-1]) # End
print(b[:-2]) # before mentioned index
print(b[-2:]) # equal & after index
print(b[3:6])
print(b[3:-2])
print(b[3:12])
print(b.count("3"))
print(b.index("3"))
# In[28]:


b="aba12"
b[-1:]
b[1:3]
b[-2:]
b.count("22")
#b.index("a")
del b

List

list=[item1,item2]
# In[29]:


##Lists
l=[1,2,3]
l1=[1,"a","12"]
l+l
len(l)
l[0]=9
l[0]
print(l)


# In[30]:


del l[1]


# In[31]:


l


# In[32]:


l.append(10)
print(l)


# In[33]:


l.insert(1,6)
print(l)


# In[34]:


l*2
l


# In[35]:


a=["c","e"]
print(a)
print(l)
x=sorted(l,reverse= False )
x


# In[36]:


a=list(range(0,7)) #start,stop-1,interval
a


# In[37]:


a=list(range(20,0,-2))
a

More on:

https://docs.python.org/3/tutorial/datastructures.html
# ## Mutable vs Immutable Objects 
#  

# ## Tuples
# 
# Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists which are mutable.

# In[38]:


# Creating a List with
# the use of Numbers
# code to test that tuples are mutable
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("Original list ", List)
 
List[3] = 77
print("Example to show mutability ", List)


# In[39]:


# code to test that tuples are immutable
 
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)

As tuples are stored in a single memory block therefore they don’t require extra space for new objects whereas the lists are allocated in two blocks, first the fixed one with all the Python object information and second a variable sized block for the data.
# In[ ]:


t=(1,23)
t2=(1,2,"a")
type(t)


# In[ ]:


import sys
a_list = []
a_tuple = ()
a_list = ["Basics", "of", "Python"]
a_tuple = ("Basics", "of", "Python")
print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))


# ### Operation & Methods applicable to all sequences
# ![image.png](attachment:image.png)

# ### Operations & Methods applicable to Mutable Sequence
# - List
# 
# ![image.png](attachment:image.png)

# ### Mapping Types objects : Dictionary
# - A mapping object represents an arbitrary collection of objects that are indexed by another collection of nearly arbitrary key values. Unlike a sequence, a mapping object is unordered and can be indexed by numbers, strings, and other objects. Mappings are **mutable**.
# 
# -  You can use any immutable object as a dictionary key value (strings, numbers, tuples, and so on). Lists, dictionaries, and tuples containing mutable objects cannot be used as keys (the dictionary type requires key values to remain constant).
# 

# In[ ]:


d={}
d={100:"monika",102:"arora"}
d


# In[ ]:


#Can we repeat key values in dic : if we repeat key it would overwrite
d={100:"monika",102:"arora",100:"PhD"}
d


# In[ ]:


print("Type= " ,type(d))


# In[ ]:


print(d.keys(),d.values())


# ### Dictionary Methods & Operations 
# ![image.png](attachment:image.png)

# In[ ]:


d[103]="viru"
d
del d[103]


# In[ ]:


d


# # Merge two Python dictionaries into one
# 
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# 
# Expected output:
# 
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# In[ ]:


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)


# ## Set Types Objects 
# A set is an unordered collection of unique items. Unlike sequences, sets provide no indexing or slicing operations. They are also unlike dictionaries in that there are no key values associated with the objects. In addition, the items placed into a set must be **immutable**. 
# - Two different set types are available: set is a mutable set, and frozenset is an immutable set. 

# In[ ]:


s={}
s={11,11,44,0,1,22,89}
s


# In[ ]:


s = set({1,2,3,4}) # set assignment
print("set=",s)
print("Type=",type(s))
s.add(9)# mutuable operation
s


# In[ ]:


s={1,2,3,4,5,6}
t={3,4}
s.issubset(t)
t.issubset(s)


# ### Methods & Operations for all set types
# ![image.png](attachment:image.png)

# ### Methods & Operations for mutuable set types¶
# ![image.png](attachment:image.png)

# In[ ]:


num = set([1, 2, 3])
num.add(4)
num

Sets:- are implemented in such a way that they don’t allow mutable objects, however, Python sets in themselves are mutable in nature.

Frozensets:- are just like sets but they can’t be changed. That is, frozensets are the immutable version of Python sets.
# In[ ]:


num = frozenset([1, 2, 3])
#num.add(4)
#num


# ### List Methods
# ![image.png](attachment:image.png)

# ## Membership Statements
# - Membership operators are operators used to validate the membership of a value. It test for membership in a sequence, such as strings, lists, or tuples.
# 

# In[ ]:


a="aapple is good for health"
b="apple"
#a in b 
#b in a # compares menbers
#b==a
#b is a # exact equal
#b is not a
#"apple" is b


# ## Multi Target Assignment

# In[ ]:


a , b = 1,2
print("a=",a )
print("b=",b)


# In[ ]:


c , s = 26.2 ,"Ashi"

print("%s age = %f"%(s,c))


# In[ ]:


a,b = b,a # swapping
a


# In[ ]:


b


# In[ ]:


### String Manipulation
a="Python is a data science tool"
b="1234"
print("This is cascading=",a+b)
print("Length of string a =",len(a)) #len() for finding length
print(a.isupper())# checks upper case
print(b.islower())# checks lower case
c=a.upper()
print("Converting a into uppercase=",c)
d=b.capitalize()
print(d)


# ### String Methods & Functions
# ![image.png](attachment:image.png)
##1. Create a List of lenght =7
#Type cast it [strings,tuples,sets and dict)

2. Write script to check whether an input string is:
    1. Ok (lenghth is b/w: 2-6) , invalid 
    2. Ok (alphanumeric) , invalid
    3. end
 
 3. create a dict with names as name and age as values. 
    

# In[ ]:




