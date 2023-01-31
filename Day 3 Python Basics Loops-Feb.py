#!/usr/bin/env python
# coding: utf-8
# For loop

for item in list_of_items
    do something to each item
# In[3]:


fruits=["apple","peach","pear"]
for i in fruits:
    print(i)
#H0w to print , say, apple pie, peach pie or pear pie


# In[4]:


for i in range(1,3):
    print(i)
    


# In[2]:


for i in range(1,3):
    print("hi")


# In[2]:


for i in range (1,4):
    print("Hello")


# # Exercise

# In[8]:


a=23
a+=1
print(a)


# In[14]:


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
  total_height += height
#print(f"total height = {total_height}")
print("total height = ", total_height)
number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)


# In[15]:


b={"a":1,"b":2}
for i in b:
    print(b.values())


# # Iteration in Loops

# In[16]:


print("List Iteration")
l = [22, 33, "Data"]
for i in l:
    print(i)


# In[17]:


# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("Python", "Data",)
for i in t:
    print(i)


# In[18]:


# Iterating over a String
print("\nString Iteration")
s = "Python"
for i in s:
    print(i)


# In[19]:


# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['red'] = 100
d['pink'] = 201
for i in d:
    print("%s %d" % (i, d[i]))


# In[20]:


# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 4, 6}
for i in set1:
    print(i)

##Iterations in loops:

print("List Iteration")
l = [22, 33, "Data"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("Python", "Data",)
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Python"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['red'] = 100
d['pink'] = 201
for i in d:
    print("%s %d" % (i, d[i]))

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 4, 6}
for i in set1:
    print(i)Using for loop with a range function.
Syntax:-

for number in range(a,b):
    print(number)
# In[8]:


for number in range(1,10):
    print(number)


# In[9]:


for number in range(1,10,3):
    print(number)


# In[22]:


## Write a script to input a numerical list of user input length
l=[]
n=int(input("Enter number of elements"))
x=int(input("Enter any number"))
for i in range (0,n):
        l.append(x)
print(l)


# In[2]:


#Create a dic with s.no as keys and colors as values
d = {}

a = int(input("Enter Sr. No: "))
b = input("Enter color: ") 
for i in range(0,a):
    d[a] = b
print(d)


# # List Comprehension in Python
# List comprehension saves time because it requires fewer lines of code than loops. It makes the code more user-friendly by keeping it simple. Furthermore, list comprehension covers the incorporation of an iterative statement into a formula.
# 
# Python provides several methods for creating lists. The list comprehension feature is one of the most effective of these methods. It allows you to create lists with just one line of code
# It can be used to create new lists from other iterable elements such as arrays, strings, tuples, lists, and so on. It consists of brackets containing the expression. To iterate over all of the elements, the system uses the for loop to execute the expression for each one
# When you use list comprehension instead of loops, you can create a list with far less effort and code.# 

# In[6]:


for i in range(8,1,-1):
    print(i)


# In[3]:


a = [i for i in range(8,1,-1)]
print(a)


# # List comprehension isn’t just for integers; it can also be applied to strings.

# In[7]:


#Script to print last element of all list members
w=["Basics", "of", "Python"]
for word in w:
    print(word[-2])


# In[11]:


#Another way: Script to print last element of all list members

w = ["Programming", "is", "easy"]
result = [word[-2] for word in w]
print(result)


# In[12]:


## Multiplication of two lists
l=[1,2]
m=[2,3]
k=[]
for i,j in l,m:
    k.append(i*j )
print(k)


# # The for loop is a common way to iterate through a list. List comprehension, on the other hand, is a more efficient way to iterate through a list because it requires fewer lines of code.
# List comprehension requires less computation power than a for loop because it takes up less space and code. This is useful when working on large programs, as efficiency becomes a major consideration when the code is lengthy.

# In[13]:


# creating the empty list
old_list = []
 # we will use the for loop to create the new list
for x in range(10):
 old_list.append(x*2)
print (old_list )


# In[14]:


# creating the set with the help of list comprehension
old_list = [x*2 for x in range(10)]
print (old_list)


# In[15]:


#Using if with List Comprehension
even_list = [ i for i in range(10) if i % 2 == 0]
print(even_list)


# In[16]:


filtered_list = [ x for x in range(50) if x % 2 == 0 if x % 5 == 0]   
#If x satisfies both conditions, x is appended to filtered_list.
print(filtered_list)


# In[17]:



l = ["even" if y%2==0 else "odd" for y in range(5)]
print(l)
# ist comprehension will check the five numbers from 0 to 4. 
#If y is divisible by 2, then even is appended to the obj list. If not, odd is appended.


# # Questions for Practice!!
# 1. Finding the elements in a list in which elements are ended with the letter ‘d’ and the length of that element is greater than 2.

# In[18]:


names = ['ABcD','Cd','acd','bbB','fb','xa','Red','Med']  # This function filter out all the strings 
#from the list that are ended with the letters ‘d’ or ‘D’.
sol = [name for name in names if name.lower().endswith('d') and len(name) > 2]
sol


# # 2. Reverse each String in a Tuple using List Comprehension

# In[19]:


a="life"
a[::]
a[:-1]
a[-1:]


# In[20]:


a = [s[::-1] for s in ('Python', 'Data', 'Analysis')]
# Display the list
print(a)


# # Dictionary comprehension
# Dictionary comprehension allows you to create dictionaries in Python, as the name implies.

# In[21]:


# using Python to showcase dictionary comprehension
 # creation of two lists to represent keys and values
keys = [1, 2, 3, 4, 5, 6]
values = ['a', 'b', 'c', 'd', 'e', 'f']
 # implementing dictionary comprehension
d = { k:v for (k,v) in zip(keys, values)}
print(d)


# # While loop
# 
# while something_is_true
#     Do somethings repeatedly
#     
# When the something_is_true becomes false, then the loop stops and comes out of it.

# In[1]:


# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1


# In[22]:


i=1 #inti
while i<4: #condit
    print(i)
    i=i+1


# In[23]:


#Exit 
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1


# In[2]:


#continue
i=0
while i<6:
    i+=1  
    if i==3:
        continue
    print(i)


# In[25]:


## Write Script that will input 5 names if name=="Name" break the loop and if name=" " continue


# In[1]:


name = input("Input a list of student heights ").split()
namei=int(name)
while namei<6:
    if name=="monika":
        break
    elif name== " ":
        continue


# In[ ]:





# In[ ]:




