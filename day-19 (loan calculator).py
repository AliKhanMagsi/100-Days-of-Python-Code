#!/usr/bin/env python
# coding: utf-8

# In[1]:


loan = 1000
interest = 0.05

for i in range(10):
  loan+=(loan * interest)
  print("Year", i + 1, "is", round(loan,2))


# In[ ]:




