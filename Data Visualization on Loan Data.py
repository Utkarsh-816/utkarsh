#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv(r"C:\Users\user\Downloads\loan_data_set.csv")


# In[3]:


data


# In[4]:


import seaborn as sns


# In[5]:


#categorical univarite


# In[6]:


data.dtypes


# In[9]:


import seaborn as sns
sns.catplot(df=data,x="Loan_Status",kind="count")


# In[10]:


df=pd.read_csv(r"C:\Users\user\Downloads\loan_data_set.csv")


# In[11]:


df


# In[12]:


import seaborn as sns
sns.catplot(data=df,x="Loan_Status",kind="count")


# In[ ]:


#numerical univarite analysis


# In[14]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))

sns.distplot(df["LoanAmount"])


# In[15]:


sns.histplot(df["LoanAmount"])


# In[17]:


sns.distplot(df["LoanAmount"],kde=True,hist=False)


# In[ ]:


#CATEGORICAL BIVARTITE


# In[18]:


#BIVARIATE NUMERICAL


# In[19]:


sns.jointplot(data=df,x="ApplicantIncome",y="LoanAmount",hue="Loan_Status")


# In[24]:


plt.figure(figsize=(10,10))
sns.jointplot(data=df,x="ApplicantIncome",y="LoanAmount",hue="Loan_Status")


# In[25]:


sns.jointplot(data=df,x="ApplicantIncome",y="LoanAmount",kind="reg")


# In[28]:


sns.pairplot(data=df)


# In[29]:


sns.pairplot(data=df,hue="Loan_Status")


# In[32]:


sns.catplot(data=df,x="Gender",y="LoanAmount",kind="box")


# In[30]:


df.dtypes


# In[33]:


sns.catplot(data=df,x="Gender",y="LoanAmount",kind="violin")


# In[34]:


sns.catplot(data=df,x="Gender",y="LoanAmount",kind="swarm")


# In[35]:


import numpy as np


# In[43]:



xpoint=np.array([0,6])
ypoint=np.array([0,250])
plt.plot(xpoint,ypoint,marker="v",linestyle="dashed")
plt.xlabel("xyz")
plt.ylabel("pqr")
plt.title("Graph")
plt.grid()


# In[46]:


y=np.ray([30,20,50,60])
plt.pie(y)


# In[47]:


y=np.array([30,20,50,60])

plt.pie(y)


# In[50]:


y=np.array([30,20,50,60])
mylab=["apple","banana","mango","kiwi"]
xyz=[.2,.2,0,0]
plt.pie(y,labels=mylab,explode=xyz)
plt.legend()


# In[ ]:





# In[ ]:





# In[ ]:




