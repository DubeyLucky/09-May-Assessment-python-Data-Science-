#!/usr/bin/env python
# coding: utf-8

# # Create a variable containing following type of data:
# (i) string
# (ii) list
# (iii) float
# (iv) tuple

# string

# In[1]:


A = "Lucky Kumar"
print(A)
type(A)


# list

# In[2]:


L = [8,'Lucky Kumar',8.8]
print(L)


# In[3]:


get_ipython().run_line_magic('whos', '')


# In[4]:


type(L)


# #Float

# In[10]:


F = 2.8

print(F)
type(F)


# tuple

# In[16]:


T=(8, 'Lucky Kumar',8.5)
print(T)
type(T)


# # Q2. Given are some following variables containing data:
# (i) var1 = ‘ ‘
# (ii) var2 = ‘[ DS , ML , Python]’
# (iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# (iv) var4 = 1.

# var1=''

# In[27]:


var1=' '
type(var1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


var4= 1
type(var4)


# # Q3. Explain the use of the following operators using an example:
# (i) /
# (ii) %
# (iii) //
# (iv) **

# (i)/ (Division) it is used for division suppose that if we want to divide any digit/number like 4/2 = 2 for example

# In[35]:


x = 4
y = 2
z= x/y
print(z)


# (ii) % (Modulo) it is used for Modulo 5 % 2 =1

# In[36]:


x = 5
y = 2
z = x % y
print(z)


# (iii) //(Floor Division) for example 10//3 = 3

# In[38]:


x = 10
y =3
z = x // y
print(z)


# (iv) ** (Power) for example 2**2 = 4

# In[39]:


x = 2**2
print(x)


# # Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.

# In[42]:


l = [12,"Lucky",2.8,"Print",12.8,888,"MCA","Loop",222,-20]
for i in l:
    print(i)
    print(type(i))


# # Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

# In[13]:


A = [1,2,3,4,5,6]
B = 2
i = 0
while i == A:
    if i % 2:
        print(i)
    else:
        print("B")
    


# # Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

# In[10]:


list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in list:
    if i % 3 == 0:
        print(i,"is divisible by 3 ")
    else:
        print(i,"it is not divisible by 3")


# # Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.

# In[ ]:


#mutable : it is when something is changeable or has the ability to changes in python. ex: list, set , dictionaries
#immutable : it is the when no change is possible over time in python ex:String, Numbers Tuples etc.,
#mutable
cities = ['Ranchi','Patna','Delhi']
for i in cities:
    print(i)
    
#immutable
'Ranchi','Patna','Delhi'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




