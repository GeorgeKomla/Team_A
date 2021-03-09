#!/usr/bin/env python
# coding: utf-8

# ## Assignment
# 
# 1. Create a class called account 
# 2. Give attributes name, balance and salary
# 3. Create a withdraw method such that it withdraws from the account balance
# 
# 4. Create class called savings_account
# 5. let it inherit from the account class
# 6. create method called deposit that deposits money into the savings account
# 7. Create another class called check_account that also inherits from the account class
# 8. modify the withdraw method in the check_account such that it deducts a fee from the check_account in addition in the amount withdrawn

# ## Groups
# 
# Group 1. Ola, Isaac, Daniel
# 
# Group 2. Juliet, George, Me
# 
# Group 3. Ernest, George Ansong

# In[1]:


class account:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.acc_balance = salary
        
    def withdraw(self, amount):
        self.acc_balance = (self.acc_balance - amount)
        return self.acc_balance
        


# In[2]:


account1 = account('Peter', 1000)


# In[3]:


account1.withdraw(90)


# In[4]:


class savings_account(account):
    def deposit(self, amount):
        self.acc_balance = self.acc_balance + amount
        return self.acc_balance


# In[5]:


savings_acc1 = savings_account('Judas', 500)


# In[6]:


savings_acc1.deposit(200)


# In[7]:


class check_account(account):
    def withdraw(self, amount, fee):
        self.acc_balance = (self.acc_balance - amount - fee)
        return self.acc_balance


# In[8]:


check_acc1 = check_account('Judas', 500)


# In[9]:


check_acc1.withdraw(200, 2)


# In[10]:


check_acc1.acc_balance


# In[11]:


check_acc1.salary


# In[ ]:




