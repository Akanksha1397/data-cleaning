#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[58]:


data =pd.read_excel('sales.xlsx')


# In[59]:


data.shape[0]


# In[60]:


data


# In[61]:


##1.find missing
print(data.isnull())


# In[62]:


print(data.isnull().sum())


# In[63]:


sns.heatmap(data.isnull())
plt.show()


# In[64]:


(data.isnull().sum()/data.shape[0])*100


# In[65]:


data.drop(columns=["ADDRESSLINE2","STATE","TERRITORY"],inplace=True)


# In[69]:


data.fillna("Not Available")
###for missing value the columns which has more than 50% of missing value we will drop them "ADDRESSLINE2","STATE","TERRITORY" and for POSTAL CODE which has 2.6% we will fill not availabe 


# In[70]:


data.isnull().sum()


# In[71]:


##2.duplicate row find
data.duplicated()


# In[72]:


## drop them 
data.drop_duplicates()


# In[74]:


#Remove duplicates but keep the LAST occurrence
data.drop_duplicates(keep='last')


# In[76]:


###standardize
data ['STATUS'] =data ['STATUS'].str.lower().str.strip()
data


# In[78]:


data ['COUNTRY'] =data ['COUNTRY'].str.upper().str.strip()
data


# In[81]:


data ['CITY'] =data ['CITY'].str.title().str.strip()
data


# In[83]:


data['DEALSIZE'] = data['DEALSIZE'].str.capitalize().str.strip()
data


# In[85]:


data['CONTACTLASTNAME'] = data['CONTACTLASTNAME'].str.title().str.strip()
data['CONTACTFIRSTNAME'] = data['CONTACTFIRSTNAME'].str.title().str.strip()
data['CUSTOMERNAME'] = data['CUSTOMERNAME'].str.title().str.strip()
data['PRODUCTCODE'] = data['PRODUCTCODE'].str.upper().str.strip()
data


# In[86]:


### for orderdate 
data['ORDERDATE'].head()


# In[89]:


data['ORDERDATE']=pd.to_datetime(data['ORDERDATE'], errors = 'coerce')
data


# In[90]:


print(data.columns)


# In[93]:


data.columns = [col.strip().upper().replace(" ", "_") for col in data.columns]
print(data.columns)


# In[96]:


data.dtypes


# In[100]:


data['ORDERNUMBER'] = pd.to_numeric(data['ORDERNUMBER'], errors='coerce')
data.dtypes


# In[104]:


data['STATUS'] = data['STATUS'].astype('category')
data['PRODUCTLINE'] = data['PRODUCTLINE'].astype('category')
data['DEALSIZE'] = data['DEALSIZE'].astype('category')
data['COUNTRY'] = data['COUNTRY'].astype('category')
data.dtypes


# In[107]:


data['PRODUCTCODE'] = data['PRODUCTCODE'].astype('string')
data['CUSTOMERNAME'] = data['CUSTOMERNAME'].astype('string')
data['CONTACTLASTNAME'] = data['CONTACTLASTNAME'].astype('string')
data['CONTACTFIRSTNAME'] = data['CONTACTFIRSTNAME'].astype('string')
data.dtypes


# In[116]:


data['POSTALCODE'] = data['POSTALCODE'].astype('string')
data['CITY'] = data['CITY'].astype('string')
data['PHONE'] = pd.to_numeric(data['PHONE'], errors='coerce')
data['ADDRESSLINE1'] = data['ADDRESSLINE1'].astype('string')
data.dtypes

