#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
import nltk


# In[2]:


nlp = spacy.load('en')


# In[3]:


doc = nlp('''''')# paragraph


# In[4]:


name = []
org = []
loc = []
date = []


# In[5]:


for x in doc.ents:
    if x.label==380:
        name.append(x.text)
    elif x.label==383:
        org.append(x.text)  
    elif x.label==384:
        loc.append(x.text)
    elif x.label==391:
        date.append(x.text) 


# In[6]:


print(name) #print the names in the parapgraph
print(org)  #print the oragnizations in the parapgraph
print(loc)  #print the locations in the parapgraph
print(date) #print the time and date in the parapgraph


# In[ ]:





# In[7]:


satp = open('C:\\Users\\Phantom\\Desktop\\sample1.txt','r')


# In[8]:


for lines in satp:
    print(lines)


# In[ ]:




