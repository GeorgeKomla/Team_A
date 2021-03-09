#!/usr/bin/env python
# coding: utf-8

# # Funtions
# 
# A function is a block of codes that performs an action.

# # What to learn
# 
# 1. Defining functions
# 
# 2. Variable scope
# 
# 3. Documentation
# 
# 4. Lamda expressions
# 
# 5. high level functions
# 
# 6. List comprehentions

# In[1]:


def cylinder_volume(height,radius): #<----- function header
    
    
    
    
    
    pi = 3.14186
    return height*pi*radius**2     #<------ function body


# In[ ]:


def words_read(word, count):
    return 
    


# In[2]:


def cylinder_volume(height,radius):
    pi = 3.14186
    return height*pi*radius**2
    


# In[3]:


cylinder_volume(1.5,3)


# In[ ]:





# In[4]:


pi # this variable has a local scope hence, cannot accessed outside the function


# In[5]:


pi_ = 22/7


# In[6]:


pi_ # Global scope


# In[7]:


def area_circle(radius):
    
    return pi_*radius**2


# In[8]:


area_circle(8)


# * Function Header
# 
# The function header always starts with the def keyword, which indicates that this is a function definition.
# 
# Then comes the function name (cylinder_volume)
# 
# Immediately after the name are parentheses that may include arguments separated by commas which in our case are height and radius
# 
# Arguments, or parameters, are values that are passed in as inputs when the function is called, and are used in the function body. 
# 
# NB: If a function doesn't take arguments, these parentheses are left empty.
# 
# The header always end with a colon :.
# 
# 
# * Funtion Body
# 
# The body of a function is the rest of the code after the header line.
# 
# Within this body, we can refer to the argument variables and define new variables, which can only be used within these indented lines.
# 
# The body will often include a return statement, which is used to send back an output value from the function to the statement that called the function.
# 
# NB: The body of a function may not contain a return stamentment but a print statement.
# 
# A return statement consists of the return keyword followed by an expression that is evaluated to get the output value for the function. 
# 
# If there is no return statement, the function simply returns None.
# 
# 
# 

# ### Variable scope
# This refers to which part of a program that a variable can be referenced or used from.

# Local variables: they are variables that can only be accessed inside the funtion
# 
# Global variables: they are variables that can be accessed ouside a function.    
# 
# The **pi** in the cylinder volume function is a local variable.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[9]:


#example
def bmi(height,weight):
    return weight/height**2


# In[10]:


bmi(1.6,56)


# In[11]:


bmi(1.9,69.78)


# In[ ]:





# In[ ]:





# In[ ]:





# ### Difference between print and return in a function

# In[12]:


def print_new_age(current_age,year):
    age = current_age +(year-2021)
    print(age)
    
    
def return_new_age(current_age,year):
    age = current_age +(year-2021)
    return age


# In[13]:


print_new_age(20,2043)


# In[14]:


return_new_age(20,2043)


# In[15]:


Afua = print_new_age(20,2043)


# In[16]:


print(Afua)


# In[17]:


Afua/2 # This will produce an error


# In[18]:


Godliver = return_new_age(20,2043)


# In[19]:


print(Godliver)


# In[20]:


Godliver/2


# In[ ]:





# In[22]:


def average_score(x):
    ave = sum(x)/len(x)
    return ave

def average_score_print(x):
    ave = sum(x)/len(x)
    print(ave)


# In[23]:


marks = [477,15,4597,45698,41,2.558,7849]

average_marks = average_score(marks)


# In[24]:


print(average_marks)


# In[25]:


marks = [477,15,4597,45698,41,2.558,7849]

average_marks_2 = average_score_print(marks)


# In[26]:


print(average_marks_2)


# ### arguments of a function
# 
# They are values passed as inputs to a function

# In[27]:


# default arguments

def cylinder_volume(height,radius, pi = 3.14186):
   
    return height*pi*radius**2


# In[28]:


cylinder_volume(23,4,22/7)


# In[29]:


cylinder_volume(23,4)


# ### passing arguments
# 1. By position
# 2. By name

# In[30]:


def bmi(height,weight):
    return weight/height**2


# In[31]:


bmi(1.76,65)


# In[32]:


bmi(65,1.76) # This is wrong


# In[33]:


bmi(weight=65,height=1.76 )


# ## Documentation Strings (Docstrings)

# In[34]:


def return_new_age(current_age,year):
    """Calculates the age of a person at a given year from 2021.
    
    INPUT:
    current_age: int, current age of the person.
    year: int, prefered year
    
    OUTPUT: 
    return_new_age: current_age +(year-2021), returns age of the person at the given year from 2021
    
    """
    age = current_age +(year-2021)
    return age


# In[35]:


def bmi(height,weight):
    """This function calculates the bmi of a person
    INPUT:
    height:float or int,height of a person in meters
    weight: float or int,weight of a person in kilograms
    """
    return weight/height**2


# In[36]:


return_new_age() # put the curser inside the bracket and press shift+tab to view the docstring 


# In[37]:


help(return_new_age)


# In[38]:


help(print)


# In[ ]:





# ## Lamda expressions (Anonymous functions)
# 
# Components of a Lambda Function
# The lambda keyword is used to indicate that this is a lambda expression.
# 
# Following lambda are one or more arguments for the anonymous function separated by commas, followed by a colon :. Similar to functions, the way the arguments are named in a lambda expression is arbitrary.
# 
# Last is an expression that is evaluated and returned in this function. This is a lot like an expression you might see as a return statement in a function.
# 
# With this structure, lambda expressions aren’t ideal for complex functions, but can be very useful for short, simple functions.
# 
# Lamda expressions are used to create anonimous functions(functions that do not have names)

# In[39]:


def square(x):
    return x**2
square(6)


# In[40]:


lambda x: x**2


# In[41]:


n = [12,4,5,6,3,4,67,8,9]


# In[42]:


square_lambda = lambda x: x**2
    


# In[43]:


square_lambda(6)


# In[44]:


lambda_bmi=lambda height,weight : weight/height**2


# In[45]:


lambda_bmi(1.7,64)


# In[ ]:





# In[46]:


square=lambda argument: argument**2


# In[47]:


square(6)


# In[48]:


BMI=lambda w,h: w/h**2


# In[49]:


BMI(62,1.5)


# ### some important higher-order built-in functions
# 
# 1. map()
# 
# **map()** is a higher-order built-in function that takes a 
# 
# function and iterable as inputs, and returns an iterator that 
# 
# applies the function to each element of the iterable.
# 
# 
# 
# 2.**filter()** is a higher-order built-in function that takes a 
# 
# function and iterable as inputs and returns an iterator with 
# 
# the elements from the iterable for which the function returns 
# 
# True.

# ### map()

# In[50]:


numbers = [ [34, 63, 88, 71, 29]  ,[90, 78, 51, 27, 45], [63, 37, 85, 46, 22], [51, 22, 34, 11, 18]]
numbers[0]          


# In[51]:


def average_score(num_list):
    return sum(num_list) / len(num_list)


# In[52]:


average = list(map(average_score,numbers))
print(average)


# In[ ]:





# ### Using lambda functions with map()

# In[53]:


n = [12,4,5,6,3,4,67,8,9]


# In[54]:


list(map(lambda x:x**2,n))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[55]:


team_points=[87,45,67,90,100,12,35,89,55,55]


# In[56]:


for point in team_points:
    add_8= point+8
    team_points
    print(point.append())


# In[ ]:





# In[ ]:





# In[57]:


def add_8(value_list):
    return value_list+8


# In[58]:


team_points_8 = list(map(add_8,team_points))
team_points_8


# In[59]:


map(add_8,team_points)


# In[60]:


team_points_8


# In[ ]:





# In[61]:


mean_l = lambda nums:sum(nums)/len(nums)

ave = list(map(mean_l,numbers))
print(ave)


# In[62]:


ave = list(map(lambda nums:sum(nums)/len(nums),numbers))
print(ave)


# ### filter()

# In[63]:


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10


# In[64]:


short_cities = list(filter(is_short, cities))
print(short_cities)


# In[65]:


is_less = lambda name: len(name) < 10
less_cities = list(filter(is_less,cities))
print(less_cities)


# ## Zip and Enumerate

# **zip** and **enumerate** are useful built-in functions that can come in handy when dealing with loops.
# They help to simplify tasks.
# 
# **zip** returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables.

# ### zip()

# In[66]:


list(zip(['a', 'b', 'c'],[1, 2, 3]))


# In[67]:


#example
list(zip(['a', 'b', 'c'], [1, 2, 3])) 


# In[68]:


t_1 = ('a',1)
t_2 = ('b',2)


# ### using the for loop with zip

# In[69]:


letters = ['a', 'b', 'c']

nums = [1, 2, 3]

colors = ['red','blue','green']



for letter, num, color in zip(letters, nums,colors):
    print("{} : {} : {} ".format(letter, num,color))


# ### Unzipping

# In[70]:


my_list = [('a', 1), ('b', 2), ('c', 3)]

letters, nums = zip(*my_list)


# In[71]:


letters


# In[72]:


nums


# ### Enumerate()

# **enumerate** is a built in function that returns an iterator 
# 
# of tuples containing indices and values of a list.
# 
# You'll often use enumerate when you want the index along with each 
# 
# element of an iterable in a loop.
# 

# In[73]:


letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)


# ### List Comprehentions
# 
# List comprehensions allow us to create a list using a for loop in one step.
# 
# You create a list comprehension with brackets [ ], including an expression to evaluate for each element in an iterable.
# 

# In[74]:


# List comprehension format: 
# [expression followed by iterable or iteration]
#Eg:


squares = [x**2 for x in range(1,10)]
print(squares)


# ### Conditionals in List Comprehensions
# 
# You can also add conditionals to list comprehensions (listcomps).
# 
# After the iterable, you can use the if keyword to check a condition in each iteration.
# 

# In[75]:


# Conditional list comprehension without 'else' format: 
# [exprssion followed by iterable followed by condition]
# Eg:
squares = [x**2 for x in range(1,9) if x % 2 == 0]
print(squares)


# Conditional List Comprehensions that includes 'else' in the
# 
# condition have a different format.
# 
# In cases like this you have to move the conditionals to the beginning of
# 
# the listcomp, right after the expression.
# 

# In[76]:


# Conditional list comprehension without 'else' format: 
# [exprssion followed by condition followed by else condition followed by iterable]
# Eg:
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(1,10)]
print(squares)


# In[ ]:





# In[ ]:





# In[ ]:





# ## Exercise

# ### Question 1
# 
# Use a list comprehension to create a new  list called first_names containing just the first names in names in lowercase.
# 

# In[77]:


#Solution
names = ['Ama Frimpong','Agyemang Duah','Kwesi Amstrong','Patrick Mensah', 'Emmanuel Doe', 'Nelson Tettey']

first_names = [name.split()[0].lower() for name in names]
print(first_names)


# In[78]:


names = ['Ama Frimpong','Agyemang Duah','Kwesi Amstrong','Patrick Mensah', 'Emmanuel Doe', 'Nelson Tettey']


# In[79]:


for name in names:
    print(name.split()[0].lower())


# In[ ]:





# In[ ]:





# In[80]:


### Explanation ( step by step)


# In[81]:


names[0].split()[0].lower()


# In[82]:


names[1].split()[0].lower()


# In[83]:


names[2].split()[0].lower()


# In[ ]:





# ### Question 2
# Use a list comprehension to create a list called multiples_3, containing the first 20 multiples of 3.

# In[84]:


# solution
multiples_3 =[i*3 for i in range(1,21)]
print(multiples_3)


# ### Question 3
# 
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.
# 

# In[85]:


scores = {
             "Rick Ampofo": 70,
             "Morty Smith": 35,
             "Samuel Sarpong": 82,
             "Jerry Rawlings": 23,
             "Bethilda Great": 98
          }


# In[86]:


# solution
passed =[name for name,score in scores.items() if score >= 65] 
print(passed)


# In[87]:


items()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




