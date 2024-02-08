#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[7]:


from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <h1>Hello, BeautifulSoup!</h1>
        <table border="1" >
  <tr>
    <th>Student</th>
    <th>Favorite Computer Language</th>  
    <th>Years of Experience</th>
  </tr>
  <tr>
    <td>Fred</td>
    <td>Kotlin</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Paula</td>
    <td>Python</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Ernst</td>
    <td>Java</td>
    <td>7</td>
  </tr>
  <tr>
    <td>Isabel</td>
    <td>C++</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Tony</td>
    <td>Pearl</td>
    <td>7</td>
  </tr>
  <tr>
    <td>Maria</td>
    <td>Cobol</td>
    <td>15</td>
  </tr>
</table>
    </body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')  
table = soup.find('table')
print(table)


# In[11]:


headers = table.find_all()
print(headers)


# In[12]:


headers = table.find_all("th")
print(headers)


# In[13]:


titles = []

for i in headers:
    title = i.text
    titles.append(title)
    
print(titles)


# In[14]:


df2 = pd.DataFrame(columns=titles)
print(df2)


# In[15]:


rows = table.find_all("tr")
print(rows)


# In[16]:


for i in rows[1:8]:
    print(i)


# In[17]:


for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(df2)
    df2.loc[l]= row

df2.head(6)

